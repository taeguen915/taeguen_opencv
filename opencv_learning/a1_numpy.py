import numpy

def show(m: str, o: numpy.ndarray):
    print(m,f"shape: {o.shape}, detype: {o.dtype}")
    print(o)


def main():
    array1 = numpy.array([1, 2, 3], dtype=numpy.int8)
    show("array1", array1)

if __name__ == "__main__":
    main()