func shuffle(nums []int, n int) []int {
	result := []int{}

	for i := 0; i < n; i++ {
		result = append(result, nums[i], nums[n+i])
	}

	return result
}