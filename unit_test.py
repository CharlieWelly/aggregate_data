import unittest
from v04 import *


class TestV03(unittest.TestCase):
    def setUp(self):
        self.dble_wb = WorkBook("./test_cases/double_statements.xlsm", "DN")
        self.dble_sheets = self.dble_wb.get_sheets()
        self.dble_ws = self.dble_sheets[0]
        self.dble_ws0 = self.dble_sheets[1]
        self.dble_ws1 = self.dble_sheets[2]
        self.dble_ws2 = self.dble_sheets[3]

        self.nodata_wb = WorkBook("./test_cases/no_data.xlsm", "DN")
        self.nodata_sheets = self.nodata_wb.get_sheets()
        self.nodata_ws = self.nodata_sheets[-1]

        self.good_wb = WorkBook("./test_cases/good.xlsm", "DN")

    def tearDown(self):
        pass

    def test_contain_dble_statement(self):
        self.assertTrue(self.dble_wb.contain_double_statement())
        self.assertFalse(self.good_wb.contain_double_statement())

    def test_get_sheets(self):
        self.assertEqual(len(self.dble_wb.get_sheets()), 5)
        self.assertEqual(len(self.good_wb.get_sheets()), 4)
        # sheets = self.dble_wb.get_sheets()
        # print(sheets[3])

    def test_WorkSheet(self):
        self.assertEqual(self.dble_ws.sheetname, "Cân đối kế toán")
        self.assertEqual(self.dble_ws.businesstype, "DN")
        self.assertEqual(self.dble_ws.start, 14)
        self.assertEqual(self.dble_ws.length, 122)
        self.assertEqual(self.dble_ws.ticker, "B82")
        self.assertEqual(self.dble_ws.interval, "Quý")

        self.assertTrue(self.dble_ws1.contain_direct_cashflow())
        self.assertEqual(self.dble_ws1.sheetname, "Lưu chuyển tiền tệ - Trực tiếp")
        self.assertEqual(self.dble_ws1.start, 14)
        self.assertEqual(self.dble_ws1.length, 28)
        self.assertEqual(
            self.dble_ws1.first_item,
            "Tiền thu từ bán hàng, Cung cấp dịch vụ và DT khác",
        )

        self.assertEqual(self.dble_ws2.sheetname, "Lưu chuyển tiền tệ - Gián tiếp")
        self.assertEqual(self.dble_ws2.start, 47)
        self.assertEqual(self.dble_ws2.length, 41)
        self.assertEqual(self.dble_ws2.ticker, "B82")
        self.assertEqual(self.dble_ws2.interval, "Quý")

    def test_todf(self):
        df1 = self.dble_ws.to_df()
        self.assertEqual(df1.shape, (5612, 7))
        # print(df1)
        df2 = self.dble_ws1.to_df()
        self.assertEqual(df2.shape, (864, 7))
        # print(df2)
        df3 = self.dble_ws2.to_df()
        self.assertEqual(df3.shape, (1312, 7))
        # print(df3)
        df4 = self.nodata_ws.to_df()
        self.assertTrue(df4.empty)

    def test_nodatetimecol(self):
        df = self.dble_ws0.to_df()
        self.assertEqual(df.shape, (1350, 7))

    def test_loopThruBook(self):
        df1 = loop_thruBook(self.dble_wb)
        self.assertEqual(df1.shape, (14476, 7))

        df2 = loop_thruBook(self.nodata_wb)
        self.assertEqual(df2.shape, (457, 7))

        df3 = loop_thruBook(self.good_wb)
        self.assertEqual(df3.shape, (2562, 7))

    def test_loopThruFile(self):
        df1 = loop_thruFile(
            "./test_cases/double_statements.xlsm",
            "DN",
        )
        self.assertEqual(df1.shape, (14476, 7))

    def test_loopThruFolder(self):
        df = loop_thruFolder("./test_cases/test_folder", "DN")
        self.assertEqual(df.shape, (18655, 7))
        # print(df)


if __name__ == "__main__":
    unittest.main()
