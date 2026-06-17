# Input: [0,0,1,1], sum = 2
# [0,0,1], sum = 1
# [0,0], sum = 0
# [0], sum = 0
# Output: 3
from colorama import Fore


def reduce_operation(featureMap):
    feat_sum = 0
    if len(featureMap) <= 1:
        return sum(featureMap)

    def redop(feat_map, fsum):
        new_arr = []

        for i in range(len(feat_map) - 1):
            new_arr.append(feat_map[i] and feat_map[i + 1])
            fsum += feat_map[i]
            if i == len(feat_map) - 2:
                fsum += feat_map[i + 1]
        if len(new_arr) <= 2:
            return fsum + new_arr[0] + new_arr[1]
        else:
            return redop(new_arr, fsum)

    return redop(featureMap, feat_sum)


if __name__ == "__main__":
    fmaps = [
        [0, 0, 1, 1],
        [1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0],
        [],
    ]
    ground_truths = [3, 1, 14, 1, 4, 0, 0]

    for i in range(len(fmaps)):
        result = None
        try:
            result = reduce_operation(fmaps[i])
            if result == ground_truths[i]:
                print(Fore.GREEN + "[TEST PASS]")
            else:
                print(Fore.RED + "[TEST FAIL]")

            print("Input: ", fmaps[i])
            print("Ground Truth: ", ground_truths[i])
            print("Actual: ", result)
            print("\n\n")
        except Exception as e:
            print("[ERROR]: ", e)
            print("\n\n")
            pass
