"""
似乎不应该直接用random作密钥，应当使用secure_token
"""


import csv
import random
import struct
import math
import decimal


# NumberOfLeastSignificantBits = 4


def WatermarkInsertion(
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

            with open(
                Filename[:-4]
                + "-Marked-Key."
                + str(Key)
                + "-r."
                + str(r)
                + "-LSB."
                + str(NumberOfLeastSignificantBits)
                + ".csv",
                "a",
                newline="",
            ) as FileMarked:
                writer = csv.writer(FileMarked)
                writer.writerow(Row)


def Mark(i, value, j):
    value = float2binary(value)
    value = list(value)
    j = len(value) - 1 - j
    if i % 2 == 0:
        value[j] = "0"
    else:
        value[j] = "1"
    value = "".join(value)
    return binary2float(value)


def Cli():
    """
    Filename = input("Input filename:")
    Key = input("Key:")
    random.seed(int(Key))  # line 2
    r = input("Target fraction of tuples marked:")
    NumberOfLeastSignificantBits = input("LSB:")
    AvailableAttributes = []
    AvailableAttributes = input("Order of attributes that can be marked:")
    """
    Filename = "test.csv"
    Key = 233
    random.seed(Key)
    r = 2
    NumberOfLeastSignificantBits = 20
    AvailableAttributes = "3 4 5 6 7"
    # """
    AvailableAttributes = list(map(int, AvailableAttributes.split()))
    x = 0
    while x < len(AvailableAttributes):
        AvailableAttributes[x] = AvailableAttributes[x] - 1
        x = x + 1
    WatermarkInsertion(
        Filename,
        int(Key),
        int(r),
        int(NumberOfLeastSignificantBits),
        AvailableAttributes,
    )


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


def testMark():
    value = float2binary(1.53700)
    print(value)
    print(Mark(1, value, 0))


if __name__ == "__main__":
    Cli()
    # filename = "test.csv"
    # print(filename[:-4])
    # testMark()
    """
    temp = float2binary(1.53700)
    print(temp)
    temp2 = binary2float(temp)
    print(temp2)
    print(math.isclose(1.53700, temp2, rel_tol=1e-4))  # float number equal(fuck
    """
