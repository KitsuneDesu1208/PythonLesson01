#'''RPG剪刀石頭布遊戲'''
#import random
#
#'''定義角色的初始屬性'''
#class Player:
#    def __init__(self, name):
#        self.name = name
#        self.hp = 100
#
#    def take_damage(self, damage):
#        self.hp -= damage
#        if self.hp < 0:
#            self.hp = 0
#
#    def is_alive(self):
#        return self.hp > 0
#
#choices = ["剪刀", "石頭", "布"]
#
#'''判斷勝負的函數'''
#def determine_winner(player_choice, computer_choice):
#    if player_choice == computer_choice:
#        return "平手"
#    elif (player_choice == "剪刀" and computer_choice == "布") or \
#         (player_choice == "布" and computer_choice == "石頭") or \
#         (player_choice == "石頭" and computer_choice == "剪刀"):
#        return "玩家"
#    else:
#        return "電腦"
#'''遊戲主函數'''
#def game():
#    player_name = input("請輸入你的名字: ")
#    player = Player(player_name)
#    computer = Player("電腦")
#
#    print(f"歡迎來到剪刀石頭布對戰, {player.name}!")
#
#    while player.is_alive() and computer.is_alive():
#        print(f"\n{player.name} 的HP: {player.hp} | 電腦的HP: {computer.hp}")
#        
#        # 玩家選擇
#        player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#        while player_choice not in choices:
#            print("無效的選擇，請重新選擇")
#            player_choice = input("請選擇 (剪刀, 石頭, 布): ")
#
#        # 電腦隨機選擇
#        computer_choice = random.choice(choices)
#        print(f"電腦選擇了: {computer_choice}")
#
#        # 判斷勝負
#        result = determine_winner(player_choice, computer_choice)
#
#        if result == "玩家":
#            print(f"{player.name} 勝利！")
#            computer.take_damage(20)
#        elif result == "電腦":
#            print("電腦勝利！")
#            player.take_damage(20)
#        else:
#            print("這局平手！")
#
#    # 遊戲結束
#    if player.is_alive():
#        print(f"\n{player.name} 獲勝了！")
#    else:
#        print("\n電腦獲勝了！")
#
## 開始遊戲
#game()

#import random
#
## 遊戲選項
#choices = ["剪刀", "石頭", "布"]
#
## 遊戲規則
#def determine_winner(player, computer):
#    if player == computer:
#        return "平手！"
#    elif (player == "剪刀" and computer == "布") or (player == "石頭" and computer == "剪刀") or (player == "布" and computer == "石頭"):
#        return "你贏了！"
#    else:
#        return "你輸了！"

# 遊戲主邏輯
#def play_game():
#    print("歡迎來到 RPG 剪刀石頭布遊戲！")
#    while True:
#        # 玩家選擇
#        player_choice = input("請選擇: 剪刀、石頭、布 (或輸入 '退出' 結束遊戲): ")
#        if player_choice == "退出":
#            print("感謝你遊玩！")
#            break
#        elif player_choice not in choices:
#            print("無效的選擇，請重新選擇！")
#            continue
#        
#        # 電腦選擇
#        computer_choice = random.choice(choices)
#        print(f"電腦選擇了: {computer_choice}")
#        
#        # 判斷勝負
#        result = determine_winner(player_choice, computer_choice)
#        print(result)
#
## 執行遊戲
#play_game()

#Before
#A, B, C,= input().split
#print(A)
#map(int,input().split)

#for color in ['red','green','blue']:
#    print(color)

python
複製程式碼
#import random
#
#class Player:
#    def __init__(self, name):
#        self.name = name
#        self.position = 0
#        self.money = 100  # 初始金錢
#        self.properties = []
#
#    def move(self, spaces):
#        self.position = (self.position + spaces) % 20  # 假設有20個格子
#        print(f"{self.name} 移動到 {self.position} 號格子。")
#
#    def buy_property(self, property_name, price):
#        if self.money >= price:
#            self.money -= price
#            self.properties.append(property_name)
#            print(f"{self.name} 購買了 {property_name}，剩餘金錢: {self.money}。")
#        else:
#            print(f"{self.name} 沒有足夠的金錢購買 {property_name}。")
#
#def roll_dice():
#    return random.randint(1, 6)
#
#def main():
#    print("歡迎來到簡易版 RPG 遊戲！")
#    player_name = input("請輸入玩家名稱: ")
#    player = Player(player_name)
#
#    while True:
#        input("按 Enter 鍵擲骰子...")
#        dice_roll = roll_dice()
#        print(f"{player.name} 擲出了 {dice_roll}。")
#        player.move(dice_roll)
#
#        # 隨機事件
#        if player.position % 5 == 0:  # 每隔5個格子有事件
#            print("你遇到了一個隨機事件！")
#            event_type = random.choice(["獲得金錢", "失去金錢"])
#            if event_type == "獲得金錢":
#                amount = random.randint(10, 50)
#                player.money += amount
#                print(f"{player.name} 獲得了 {amount} 金錢，剩餘金錢: {player.money}。")
#            else:
#                amount = random.randint(10, 50)
#                player.money -= amount
#                print(f"{player.name} 失去了 {amount} 金錢，剩餘金錢: {player.money}。")
#
#        # 購買地產
#        if player.position % 3 == 0 and player.position != 0:  # 每隔3個格子可以購買地產
#            property_price = random.randint(20, 70)
#            print(f"你到達了一個地產格子！這個地產的價格是 {property_price}。")
#            buy_decision = input("你想購買這個地產嗎？(y/n): ")
#            if buy_decision.lower() == 'y':
#                player.buy_property(f"地產{player.position}", property_price)
#
#        # 結束條件
#        if player.money <= 0:
#            print(f"{player.name} 已經破產，遊戲結束！")
#            break
#
#if __name__ == "__main__":
#    main()