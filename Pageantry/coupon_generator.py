import random


class CouponGenerator():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV1234567890`-=~!@#$%^&*()_+?"

    def generator(self, numbers_coupons):
        length_of_coupon = 9
        number_of_coupons = numbers_coupons
        coupon_codes = []
        for x in range(0,number_of_coupons):
            coupon = ""

            for x in range(0,length_of_coupon):
                coupon += random.choice(self.char)
            coupon_codes.append(coupon)
        
        return coupon_codes



