nl = sorted(nums1+nums2)
        l = len(nl)
        if l % 2 == 0:
            i = nl[(l//2)-1]
            j = nl[l//2]
            return float((i+j)/2.0)
        else:
            return nl[l//2
#could also use num1.extends(nums2)
