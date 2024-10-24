def Insert_Date(datas):
    data = {}
    while True :
        data["name"] = input("請輸入名稱 : ")
        data["apartment"] = input("請輸入部門別 : ")
        data["age"] = input("請輸入年紀 : ")
        data["phone"] = input("請輸入手機 : ")
        datas.append(data)
        if input("是否繼續輸入資料 ? (Y/N) : ").lower() == "n":
            break
def Search_Data(datas):
    search_data = input("請輸入要查詢的名字 : \n\n")
    found = False  # 標記是否找到資料
    print(f"{'--- 查詢結果 ---':^40}")
    print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
    print("----------------------------------------")
    for data in datas:
        if data["name"] == search_data :
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}\n\n")
            found = True  # 找到資料後標記為 True

    if not found:
        print("沒有找到該資料。\n\n")

def Update_Data(datas):
    update_data = input("請輸入要修改的姓名 : \n\n")
    found = False  # 標記是否找到資料
    print(f"{'--- 查詢結果 ---':^40}")
    print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
    print("----------------------------------------")
    for data in datas:
        if data["name"] == update_data :
            found = True  # 找到資料後標記為 True
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}\n\n")

            print("1. 修改姓名")
            print("2. 修改部門")
            print("3. 修改年齡")
            print("4. 修改手機")

            update_item = input("請輸入要修改的項目 : \n\n")
            if update_item  == "1":
                data["name"] = input("請輸入新的姓名 : ")
            elif update_item == "2" :
                data["apartment"] = input("請輸入新的部門 : ")
            elif update_item == "3" :
                data["age"] = input("請輸入新的年紀 : ")
            elif update_item == "4" :
                data["phone"] = input("請輸入新的手機 : ")
            else :
                print("輸入錯誤!")

            # 顯示修改後的資料
            print(f"{'--- 修改後的資料 ---':^40}")
            print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
            print("----------------------------------------")
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}\n\n")
            break  # 找到並修改後，跳出迴圈


    if not found:
        print("沒有找到該資料。\n\n")


def Delete_Data():
    pass



def Show_Data():
    pass



if __name__ == "__main__" :
    datas = []

    while True :
        print("--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        print("-------------------------")

        operation_choies = input("請選擇功能 : ")

        if operation_choies == "1":
            Insert_Date(datas)

        elif operation_choies == "2" :
            Search_Data(datas)

        elif operation_choies == "3" :
            Update_Data(datas)

        elif operation_choies == "4" :
            Delete_Data(datas)

        elif operation_choies == "5" :
            Show_Data(datas)

        elif operation_choies == "6" :
            break

        else :
            print("請輸入正確系統代碼!!\n\n")