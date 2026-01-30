class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i + 1:]:
                return [i, nums.index(complement, i + 1)]
        return []   
    

# Time Complexity: O(n^2) in the worst case due to the 'in' operator and slicing inside the loop.
# Space Complexity: O(n) because slicing 'nums[i+1:]' creates a temporary copy of the list elements.
# This solution iterates through each element and checks if the complement exists in the remaining part of the list.
# If found, it returns the indices of the two numbers that add up to the target.

# Zaman Karmaşıklığı: En kötü durumda O(n^2); çünkü döngü içinde dilimleme (slicing) ve 'in' operatörü kullanılıyor.
# Alan (Space) Karmaşıklığı: O(n); çünkü 'nums[i+1:]' dilimlemesi listenin elemanlarının geçici bir kopyasını oluşturur.
# Bu çözüm, her elemanı dolaşır ve tamamlayanın (complement) listenin geri kalan kısmında olup olmadığını kontrol eder.
# Eğer bulunursa, hedef (target) toplamını veren iki sayının indekslerini döndürür.