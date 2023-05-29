"""
pip install 拒绝访问可能是因为存在打开的python终端
"""

import csv
import random
import struct
import math
import decimal
from scipy.stats import binom
from bisect import bisect_left


TotalCount = 0
MatchCount = 0
Alpha = 0.0


def float2binary(num):
    y = struct.unpack("<I", struct.pack("<f", num))
    z = format(y[0], "b")
    while len(z) < 32:
        z = "0" + z
    return z


def binary2float(num):
    num = int(num, 2)
    y = struct.unpack("<f", struct.pack("<I", num))
    return y[0]


def WatermarkDetection(
    Filename, Key, r, NumberOfLeastSignificantBits, AvailableAttributes
):
    with open(
        Filename,
        newline="",
    ) as FileSource:
        Reader = csv.reader(FileSource)
        for row in Reader:
            Row = row

            if random.randint(2, Key) % r == 0:
                AvailableAttributesIndex = random.randint(2, Key) % len(
                    AvailableAttributes
                )
                BitIndex = random.randint(2, Key) % NumberOfLeastSignificantBits
                global TotalCount
                global MatchCount
                TotalCount = TotalCount + 1
                MatchCount = MatchCount + Match(
                    random.randint(2, Key),
                    float(Row[AvailableAttributes[AvailableAttributesIndex]]),
                    BitIndex,
                )
                """
                MarkedFloatLength = (
                    decimal.Decimal(row[AvailableAttributes[AvailableAttributesIndex]])
                    .as_tuple()
                    .exponent
                )

                Row[AvailableAttributes[AvailableAttributesIndex]] = Mark(
                    random.randint(2, Key),
                    float(Row[AvailableAttributes[AvailableAttributesIndex]]),
                    BitIndex,
                )

                Row[AvailableAttributes[AvailableAttributesIndex]] = format(
                    Row[AvailableAttributes[AvailableAttributesIndex]],
                    "." + str(abs(MarkedFloatLength)) + "f",
                )
                """


def Match(i, value, j):
    value = float2binary(value)
    value = list(value)
    j = len(value) - 1 - j
    if i % 2 == 0:
        if value[j] == "0":
            return 1
    else:
        if value[j] == "1":
            return 1
    return 0


def Cli():
    """
    Filename = input("Input filename:")
    Key = input("Key:")
    random.seed(int(Key))  # line 2
    r = input("Target fraction of tuples marked:")
    NumberOfLeastSignificantBits = input("LSB:")
    AvailableAttributes = []
    AvailableAttributes = input("Order of attributes that can be marked:")
    global Alpha
    Alpha= Input("Threshold parameter for detecing a watermark:")
    """
    Filename = "test-Marked-Key.233-r.2-LSB.20.csv"
    print(Filename)
    Key = 233
    random.seed(Key)
    r = 2
    NumberOfLeastSignificantBits = 20
    AvailableAttributes = "3 4 5 6 7"
    global Alpha
    Alpha = 0.05
    # """
    AvailableAttributes = list(map(int, AvailableAttributes.split()))
    x = 0
    while x < len(AvailableAttributes):
        AvailableAttributes[x] = AvailableAttributes[x] - 1
        x = x + 1
    WatermarkDetection(
        Filename,
        int(Key),
        int(r),
        int(NumberOfLeastSignificantBits),
        AvailableAttributes,
    )


def tau(omega, alpha):
    t = 0
    for i in range(omega // 2 + 1):
        cdf = binom.cdf(omega - i, omega, 0.5) - binom.cdf(i - 1, omega, 0.5)
        if cdf >= 1 - alpha:
            t = i
        else:
            break
    return t


def Judge():
    global MatchCount, TotalCount, Alpha
    Tau = tau(TotalCount, Alpha)
    if MatchCount < Tau or MatchCount > TotalCount - Tau:
        print("suspect piracy")
    print("Done!")


if __name__ == "__main__":
    Cli()
    Judge()
