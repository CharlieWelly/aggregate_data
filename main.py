import sys
import v04
import time

MODES = {
    "-n1": "NHOM_1",
    "-n2": "NHOM_2",
    "-n3": "NHOM_3",
    "-n4": "NHOM_4",
}


def main():
    start = time.perf_counter()
    args = sys.argv[1:]
    mode = args[1]
    name = args[2]
    v04.setUp(MODES[mode])
    if args[0] == "-folder":
        df = v04.loop_thruFolder(name)
    if args[0] == "-file":
        df = v04.loop_thruFile(name)

    df1 = v04.toUserFriendly(df)

    df.to_csv("./%s_developer_aggregated.csv" % MODES[mode])
    df1.to_excel("./%s_userfriendly_aggregated.xlsx" % MODES[mode])
    print("time elapse: %s" % (time.perf_counter() - start))


if __name__ == "__main__":
    main()
