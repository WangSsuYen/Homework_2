def Insert_Date(datas):
    while True :
        data = {}
        data["name"] = input("請輸入名稱 : ")
        data["apartment"] = input("請輸入部門別 : ")
        data["age"] = input("請輸入年紀 : ")
        data["phone"] = input("請輸入手機 : ")
        datas.append(data)
        if input("是否繼續輸入資料 ? (Y/N) : ").lower() == "n":
            break

def Search_Data(datas):
    search_data = input("請輸入要查詢的名字 : ")
    found = False  # 標記是否找到資料
    print(f"{'--- 查詢結果 ---':^40}")
    print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
    print("----------------------------------------")
    for data in datas:
        if data["name"] == search_data :
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}")
            found = True  # 找到資料後標記為 True

    if not found:
        print("沒有找到該資料。")

def Update_Data(datas):
    update_data = input("請輸入要修改的姓名 : ")
    found = False  # 標記是否找到資料
    print(f"{'--- 查詢結果 ---':^40}")
    print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
    print("----------------------------------------")
    for data in datas:
        if data["name"] == update_data :
            found = True  # 找到資料後標記為 True
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}")

            print("1. 修改姓名")
            print("2. 修改部門")
            print("3. 修改年齡")
            print("4. 修改手機")

            update_item = input("請輸入要修改的項目 : ")
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
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}")
            break  # 找到並修改後，跳出迴圈


    if not found:
        print("沒有找到該資料。")


def Delete_Data(datas):
    data_name = input("請輸入要刪除的姓名 : ")
    del_data = None  # 初始化 del_data
    for data in datas :
        if data_name == data["name"]:
            del_data = data
            break

    if del_data is not None :
        datas.remove(del_data)
        print(f"{data_name} 的資料已刪除!")
    else:
        print("查無此人!")


def Show_Data(datas):
    if not datas :
        print("目前無資料。")
    else:
        print(f"{'--- 查詢結果 ---':^40}")
        print(f"{'姓名':<10}{'部門':<10}{'年紀':<10}{'手機':<10}")
        print("----------------------------------------")
        for data in datas:
            print(f"{data['name']:<10}{data['apartment']:<10}{data['age']:<10}{data['phone']:<10}")



if __name__ == "__main__" :
    datas = []

    while True :
        print("\n\n--- 人事資料管理系統 ---")
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
            print(    '''
                                   _ooOoo_         \n
                                  o8888888o       \n
                                  88" . "88       \n
                                  (| -_- |)       \n
                                  O\  =  /O       \n
                                ___/`---'\____    \n
                             .'  \\|     |//  `.  \n
                            /  \\|||  :  |||//  \  \n
                            /  _||||| -:- |||||_  \ \n
                            |   | \\\  -  /// |   | \n
                            | \_|  ''\---/''  |   | \n
                            \  .-\__       __/-.  / \n
                            ___`. .'  /--.--\ `. . __ \n
                        ."" '<  `.___\_<|>_/__.'  >'"". \n
                        | | :  `- \`.;`\ _ /`;.`/ - ` : | |  \n
                        \  \ `-.   \_ __\ /__ _/   .-` /  /  \n
                ======`-.____`-.___\_____/___.-`____.-'======  \n
                                    `=---='  \n
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n
                            佛祖保佑       永無BUG  \n
                ''')
            break

        else :
            print("請輸入正確系統代碼!!")