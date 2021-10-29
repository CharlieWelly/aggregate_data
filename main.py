import sys
import v04

MODES = {
    "-n1": "NHOM_1",
    "-n2": "NHOM_2",
    "-n3": "NHOM_3",
    "-n4": "NHOM_4",
}


def main():
    args = sys.argv[1:]
    mode = args[1]
    name = args[2]
    v04.setUp(MODES[mode])
    if args[0] == "-folder":
        df = v04.loop_thruFolder(name)
    if args[0] == "-file":
        df = v04.loop_thruFile(name)

    df1 = v04.toUserFriendly(df)

    df.to_csv("./developer_aggregated.csv")
    df1.to_excel("./userfriendly_aggregated.xlsx")


if __name__ == "__main__":
    main()
