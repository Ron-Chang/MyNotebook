from datetime import date

class Donate:

    today = date.today()

    # 屬性默認為類屬性（可以給直接被類本身調用）
    y = today.year
    m = today.month
    d = today.day

    Streamer_name = "Ronhsien Chang"

    def __init__(self, sponsor, price, register_y=y, register_m=m, register_d=d):

        self.sponsor = sponsor;
        self.price = price;
        self.donateDate = register_y,register_m,register_d

    def __str__(self):
        return f"Sponsored Name: {self.sponsor}"

    # 實例化方法（必須實例化類之後才能被調用）
    def Notifications(self): # self : 表示實例化類後的地址id
        response = f"{self.price:,} was donated by {self.sponsor} - {self.donateDate[0]}/{self.donateDate[1]}/{self.donateDate[2]}"
        return response

class DonateEncapsulation:

    today = date.today()

    # 屬性默認為類屬性（可以給直接被類本身調用）
    y = today.year
    m = today.month
    d = today.day

    Streamer_name = "Ronhsien Chang"

    def __init__(self, sponsor, price, register_y=y, register_m=m, register_d=d):

        self._sponsor = sponsor;
        self._price = price;
        self.donateDate = register_y,register_m,register_d

    def __str__(self):
        return f"Sponsored Name: {self._sponsor}"

    # 實例化方法（必須實例化類之後才能被調用）
    def Notifications(self): # self : 表示實例化類後的地址id
        response = f"{self._price} was donated by {self._sponsor} - {self.donateDate[0]}/{self.donateDate[1]}/{self.donateDate[2]}"
        return response


def main(opt):

    option = (Donate("RON",10000), DonateEncapsulation("RON",10000))

    if opt == 0:
        print("Program has been terminated")
        exit()
    else:
        instance = option[opt-1]

    print(f"Noticification: {instance.Notifications()}")

    instance.sponsor = "THIEF"
    instance.price = 10_000_000
    info ="""
   --- Try to change the variables ---
    instance.sponsor = "THIEF"
    instance.price = "10_000_000"
   -----------------------------------
"""
    print(info)
    print(f"Noticification: {instance.Notifications()}")

if __name__ == "__main__":

    info = """
-------------------------------------
 It is a encapsulation demonstration
     這是一個 [類] - [封裝] 演示
-------------------------------------
    1. Normal variable 無封裝變數
    2. Encapsulate variable 封裝變數

    0. Extract 脫離

-------------------------------------
"""
    print(info)
    while True:

        opt = input(">>> ")

        if opt in ["1","2","0"]:
            main(int(opt))
        else:
            input_Err = "Input 1, 2 or 0"
            print(input_Err)
