import os
import re
from collections import namedtuple
import pandas as pd
from openpyxl import load_workbook

DOUBLE_STATEMENT = "A48"
CASHFLOW_STATEMENT_CHECK = "A15"
TICKER = "B8"
INTERVAL = "E8"

StatementDesign = namedtuple(
    "StatementDesign", ["name", "start", "first_item", "length"]
)

BS = StatementDesign("Cân đối kế toán", 14, "TÀI SẢN NGẮN HẠN", 122)
IS = StatementDesign("Kết quả Kinh doanh", 14, "Doanh số", 25)
CF = StatementDesign("Lưu chuyển tiền tệ", None, None, None)
CFDR = StatementDesign(
    "Lưu chuyển tiền tệ - Trực tiếp",
    14,
    "Tiền thu từ bán hàng, Cung cấp dịch vụ và DT khác",
    28,
)
CFID = StatementDesign("Lưu chuyển tiền tệ - Gián tiếp", 14, "Lãi trước thuế", 41)
CFID2 = StatementDesign("Lưu chuyển tiền tệ - Gián tiếp", 47, "Lãi trước thuế", 41)
SD = StatementDesign("Thuyết minh", 14, "Tiền", 157)

STATEMENT = {
    "Cân đối kế toán": BS,
    "Kết quả Kinh doanh": IS,
    "Lưu chuyển tiền tệ": CF,
    "Lưu chuyển tiền tệ - Trực tiếp": CFDR,
    "Lưu chuyển tiền tệ - Gián tiếp": CFID,
    "Lưu chuyển tiền tệ - Gián tiếp - 2": CFID2,
    "Thuyết minh": SD,
}


class WorkBook(object):
    def __init__(self, file, businesstype):
        self.wb = load_workbook(file)
        self.sheetnames = self.wb.sheetnames
        assert len(self.sheetnames) == 4
        self.businesstype = businesstype

    def __getitem__(self, key):
        return self.wb[key]

    def contain_double_statement(self):
        val = self.wb["Lưu chuyển tiền tệ"][DOUBLE_STATEMENT].value
        return val and val.strip() == CFID.first_item

    def export_sheets(self):
        sheets = []
        for sheetname in self.sheetnames:
            if not sheetname == "Lưu chuyển tiền tệ":
                sheets.append(WorkSheet(self, sheetname))
            else:
                sheets.append(CashFlowSheet(self, sheetname))
                if self.contain_double_statement():
                    sheets.append(CashFlowSheet2(self, sheetname))
        return sheets


class WorkSheet(object):
    def __init__(self, wb, sheetname):
        self.wb = wb
        self.sheetname = sheetname
        self.content = self.wb[self.sheetname]
        self.businesstype = self.wb.businesstype
        self.start = STATEMENT[self.sheetname].start
        self.length = STATEMENT[self.sheetname].length
        self.first_item = STATEMENT[self.sheetname].first_item
        self.ticker = self.content[TICKER].value.strip()
        self.interval = self.content[INTERVAL].value.strip()

    def __str__(self):
        return "<Worksheet: %s>" % self.sheetname

    def to_df(self):
        df = pd.DataFrame(self.content.values)
        df.iloc[10, 0] = "items"
        df.columns = df.iloc[10]
        df = df.iloc[self.start : self.start + self.length]
        df.dropna(axis="columns", how="all", inplace=True)
        df.dropna(axis="index", how="all", inplace=True)
        df.reset_index(drop=True, inplace=True)
        df["items"] = df["items"].str.strip()
        if len(df.columns) > 1:
            self.drop_nodatetimecol(df)
            self.validate_design(df)
            df = pd.melt(df, id_vars=["items"], var_name="year", ignore_index=False)
            df["statement_name"] = self.sheetname
            df["statement_interval"] = self.interval
            df["business_type"] = self.businesstype
            df["ticker"] = self.ticker
            return df
        else:
            return pd.DataFrame()

    def drop_nodatetimecol(self, df):
        pattern = re.compile(r"\s*(?:Q\d\s*/)?\s*\d{4}\s*")
        for col in df.columns[1:]:
            if not pattern.match(col):
                df.drop(columns=col, inplace=True)

    def validate_design(self, df):
        try:
            first_item = df.loc[0, "items"]
            assert first_item == self.first_item
        except AssertionError as e:
            print(f"{self.ticker} {self.sheetname} has invalid design")
            print(f"expect {first_item}, but receive {self.first_item}")
            raise e


class CashFlowSheet(WorkSheet):
    def __init__(self, wb, sheetname):
        WorkSheet.__init__(self, wb, sheetname)

        if self.contain_direct_cashflow():
            self.sheetname = "Lưu chuyển tiền tệ - Trực tiếp"
        else:
            self.sheetname = "Lưu chuyển tiền tệ - Gián tiếp"

        self.start = STATEMENT[self.sheetname].start
        self.length = STATEMENT[self.sheetname].length
        self.first_item = STATEMENT[self.sheetname].first_item

    def contain_direct_cashflow(self):
        val = self.content[CASHFLOW_STATEMENT_CHECK].value
        return val and val.strip() == CFDR.first_item


class CashFlowSheet2(WorkSheet):
    def __init__(self, wb, sheetname):
        WorkSheet.__init__(self, wb, sheetname)
        self.sheetname = "Lưu chuyển tiền tệ - Gián tiếp"
        self.subfix = " - 2"
        self.start = STATEMENT[self.sheetname + self.subfix].start
        self.length = STATEMENT[self.sheetname + self.subfix].length
        self.first_item = STATEMENT[self.sheetname + self.subfix].first_item


def loop_thruBook(wb):
    return pd.concat([ws.to_df() for ws in wb.export_sheets()])


def loop_thruFile(excel_file, businesstype):
    wb = WorkBook(excel_file, businesstype)
    return pd.concat([ws.to_df() for ws in wb.export_sheets()])


def loop_thruFolder(folder, businesstype):
    files = os.listdir(folder)
    pat = re.compile(r".*FiinPro_BCTC_.*")
    df = pd.concat(
        [
            loop_thruFile(f"{folder}/{file}", businesstype)
            for file in files
            if pat.match(file)
        ]
    )
    return df


if __name__ == "__main__":
    import sys

    if sys.argv[1] == "-d":
        df = loop_thruFolder(sys.argv[2], "DN")
        df.to_csv("./qrtly.csv")
    if sys.argv[1] == "-f":
        df = loop_thruFile(sys.argv[2], "DN")
        print(df)
