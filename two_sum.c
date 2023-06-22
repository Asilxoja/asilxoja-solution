
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *result = (int *)malloc(2 * sizeof(int));
    int i, complement;
    int hashmap[10000] = {0};
    for(i = 0; i < numsSize; i++){
        complement = target - nums[i];
        if(hashmap[complement] != 0){
            result[0] = i;
            result[1] = hashmap[complement] - 1;
            break;
        }
        hashmap[nums[i]] = i + 1;
    }
    *returnSize = 2;
    return result;
}

int main(){
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int *result = twoSum(nums, numsSize, target, &returnSize);
    printf("[%d, %d]", result[0], result[1]);
    return 0;
}
}