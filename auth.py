from SelectPurpose import SelectPurpose
from TopPage import TopPage
from EntryStay import EntryStay
from EntryBanquet import Enkai_Input
from QuotationStay import QuotationStay
from QuotationBanquet import Enkai_Cinfirm

# トップページから利用用途画面へ
def pagemove_top_select(self,name,email):
    SelectPurpose(self,name,email)

# 利用用途画面から宿泊の入力画面へ
def pagemove_select_entrystay(self,name,email):
    EntryStay(self,name,email)
    
# #利用用途画面から宴会入力画面へ
def pagemove_select_entrybanquet(self,name,email):
    Enkai_Input(self,name,email)
    
#確認画面からトップ
def reset_quotationstay_entry(self):
    TopPage(self)

#見積もり画面から入力画面に行く
def retuen_quotationstay_entrystay(self,name, email,numAdult,numChild,room,dinner,numStay,Adultplan,Childplan,checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa):
    
    EntryStay(self,name, email,numAdult,numChild,room,dinner,numStay,Adultplan,Childplan,checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa)

def retuen_quotationstay_entrybanque(self,name, email,all_num,cource,staynum,roomgrade1,roomgrade2,nominum,nomitime,add_menu1,add_menu2,add_menu3,nijikai_plan,nijikai_num):
    Enkai_Input(self,name, email,all_num,cource,staynum,roomgrade1,roomgrade2,nominum,nomitime,add_menu1,add_menu2,add_menu3,nijikai_plan,nijikai_num)

#入力画面から利用用途
def retuen_entry_select(self,name,email):
    SelectPurpose(self,name,email)
#利用用途からトップページ
def retuen_select_top(self,name,email):
    TopPage(self,name,email)

    

# # 宿泊入力画面から宿泊見積画面へ
def pagemove_entrystay_quotationstay(self,name, email,numAdult,numChild,numStay,room,dinner,Adultplan,Childplan,checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa):
    quotationtotal_list=[]
    for i in range(len(numAdult)):
        quotationtotal = int(numAdult[i]) * (Adultplan[i]) * int(numStay[i]) + int(checkin_option[i]) + int(bedrockButh_option[i]) + int(peterAdult_option[i]) + int(parkAdult_option[i]) + int(tennis_option[i]) + int(hotSpringRental_option[i]) + int(numChild[i]) * int(Childplan[i]) * int(numStay[i]) + int(checkin_option[i]) + int(bedrockButh_option[i]) + int(peterChild_option[i]) + int(parkChild_option[i]) + int(tennis_option[i]) + int(hotSpringRental_option[i]) + int(dogone_option[i])
        quotationtotal_list.append(quotationtotal)
        
    
    QuotationStay(self,name, email,numAdult,numChild,numStay,room,dinner,Adultplan,Childplan,checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa,quotationtotal_list)
# 宴会入力画面から宴会見積画面へ
def pagemove_entrybanquet_quotationbanquet(self,name, email,all_num,courcename,courcemoney,staynum,roomgrade1,roomgrade2,roomgrade1num,roomgrade2num,nominum,nomitime,add_menu1,add_menu2,add_menu3,menu1_num,menu2_num,menu3_num,nijikai_plan,nijikai_num,nijikai_money):
    
    nostay =  all_num - staynum
    staymoney = staynum * courcemoney
    nostaymoney =  nostay * (0.7 * courcemoney)
    nomitotal = (((nomitime // 2) + (nomitime % 2)) * 2800) * nominum
    nijikaitotal = nijikai_num * nijikai_money
    roomgrade1total = roomgrade1 * roomgrade1num 
    roomgrade2total = roomgrade2 * roomgrade2num
    add_menu1_total = add_menu1*menu1_num
    add_menu2_total = add_menu2*menu2_num
    add_menu3_total = add_menu3*menu3_num
    
    Banquettotal =  int(staymoney + nostaymoney + nomitotal + add_menu1_total + add_menu2_total + add_menu3_total + nijikaitotal + roomgrade1total + roomgrade2total)

    print(Banquettotal)
    
    from QuotationBanquet import Enkai_Cinfirm
    Enkai_Cinfirm(self,name, email,all_num,courcename,courcemoney,staynum,roomgrade1,roomgrade2,roomgrade1num,roomgrade2num,nominum,nomitime,add_menu1,add_menu2,add_menu3,menu1_num,menu2_num,menu3_num,nijikai_plan,nijikai_num,nijikai_money,staymoney,nostaymoney,nomitotal,nijikaitotal,roomgrade1total,roomgrade2total,add_menu1_total,add_menu2_total,add_menu3_total,Banquettotal)




import os
from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#宿泊のメール送信
def Stay_Send_email(name, email,numAdult,numChild,numStay,room,dinner,Adultplan,Childplan,checkin_option, bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, parkChild_option, tennis_option, hotSpringRental_option, dogone_option, numdog, dogoneSpa,quotationtotal):#見積もり結果、日付、見積もりの内容

    # リストを辞書に変換
    room_details = {
        'numAdult': numAdult,
        'numChild': numChild,
        'room': room,
        'dinner': dinner,
        'numStay': numStay,
        'Adultplan': Adultplan,
        'Childplan': Childplan,
        'checkin_option': checkin_option,
        'bedrockButh_option': bedrockButh_option,
        'peterAdult_option': peterAdult_option,
        'peterChild_option': peterChild_option,
        'parkAdult_option': parkAdult_option,
        'parkChild_option': parkChild_option,
        'tennis_option': tennis_option,
        'hotSpringRental_option': hotSpringRental_option,
        'dogone_option': dogone_option,
        'numdog': numdog,
        'dogoneSpa': dogoneSpa,
        'quotationtotal': quotationtotal
    }

    # 部屋ごとにデータをまとめたリストを作成
    room_data = []
    for i in range(len(numAdult)):  # 部屋数だけループ
        room_info = {key: room_details[key][i] for key in room_details}
        room_data.append(room_info)

    # データの例を表示
    for i, room in enumerate(room_data, 1):
        print(f"【部屋 {i}】")
        for key, value in room.items():
            print(f"{key}: {value}")
        print()

    # 部屋1の情報にアクセス
    room1 = room_data[0]
    print("部屋1の詳細情報:", room1)
    Stay_Send_email2(name, email,room_data)


def Stay_Send_email2(name, email,room_data):
    # メールアカウントの設定
    ID = 'a.tazawa.sys24@morijyobi.ac.jp'
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587

    # メール本文の作成（HTML形式）
    body = f'''
    <h2>八幡平ハイツ　見積もり結果</h2>
    <p>{name}様</p>
    <p>以下がご希望の見積もり結果です。</p>
    '''

    total_price = 0

    # 部屋ごとにループして見積もり内容を追加
    for i, room in enumerate(room_data, 1):
        body += f'''
        <hr>
        <h3>【部屋 {i}】</h3>
        <ul>
            <li>人数：大人 {room['numAdult']} 名 / 子供 {room['numChild']} 名</li>
            <li>泊数：{room['numStay']}泊</li>
            <li>部屋：{room['room']}、夕食：{room['dinner']}</li>
            <li>プラン：大人 {room['Adultplan']}円 / 子供 {room['Childplan']}円</li>
            <li>チェックイン：{room['checkin_option']}円</li>
            <li>岩盤浴：{room['bedrockButh_option']}円</li>
            <li>パターゴルフ：大人 {room['peterAdult_option']}円 / 子供 {room['peterChild_option']}円</li>
            <li>パークゴルフ：大人 {room['parkAdult_option']}円 / 子供 {room['parkChild_option']}円</li>
            <li>テニス：{room['tennis_option']}円</li>
            <li>貸し切り温泉：{room['hotSpringRental_option']}円</li>
            <li>ドッグわん：{room['numdog']} 匹（{room['dogone_option']}円）</li>
            <li>スパ利用：{room['dogoneSpa']}円</li>
            <li><strong>部屋ごとの合計金額：{room['quotationtotal']}円</strong></li>
        </ul>
        '''
        total_price += room['quotationtotal']

    # 合計金額と早割情報の追加
    body += f'''
    <hr>
    <h3>【全体の合計金額】：{total_price}円</h3>
    <p><strong>早割について：</strong><br>
    ・60日前予約 → 10%割引<br>
    ・90日前予約 → 15%割引</p>
    <p>ご予約は <a href="https://8mantai.jp/">公式サイト</a> からどうぞ！</p>
    '''

    # メールメッセージの準備
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    msg['Subject'] = '見積もり確認メール'
    msg['From'] = ID
    msg['To'] = email

    try:
        # メールサーバーに接続
        server = SMTP(HOST, PORT)
        server.starttls()  # 暗号化通信
        server.login(ID, PASS)  # ログイン
        server.send_message(msg)  # メール送信
        print("メール送信成功")
    except Exception as e:
        print("メール送信エラー:", e)
    finally:
        server.quit()  # サーバー切断
    
#宴会のメール送信



import os
from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def Banquet_Send_email(name, email,all_num,courcename,courcemoney,staynum,roomgrade1,roomgrade2,roomgrade1num,roomgrade2num,nominum,nomitime,add_menu1,add_menu2,add_menu3,menu1_num,menu2_num,menu3_num,nijikai_plan,nijikai_num,nijikai_money,staymoney,nostaymoney,nomitotal,nijikaitotal,roomgrade1total,roomgrade2total,add_menu1_total,add_menu2_total,add_menu3_total,Banquettotal):#見積もり結果、日付、見積もりの内容
    # メールアカウントの設定
    ID = 'h.komame.sys24@morijyobi.ac.jp'
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    # メール本文の作成（HTML形式）
    body = f'''
    <h2>八幡平ハイツ　見積もり結果</h2>
    <p>{name}様</p>
    <p>ご利用ありがとうございます。見積もり結果は以下の通りです。</p>
    <p>〖見積もり内容〗<br>-------------------------------------------------------------------------------------------<br>
    人数:{all_num}名<br>
    コース名：{courcename}／{courcemoney}円<br>
    宿泊人数:{staynum}人／{staymoney}円<br>
    ※宿泊しない方は、30%オフ／計{nostaymoney}円<br>
    
    部屋グレード：<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;岩手山展望露天風呂付和室【一部屋{roomgrade1}】:{roomgrade1num}人／{roomgrade1total}円<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;檜の内風呂付和洋室【一部屋{roomgrade2}】:{roomgrade2num}人／{roomgrade2total}円<br>
    飲み放題：{nomitime}時間{nominum}人／{nomitotal}円<br>
    追加料理：<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;八幡平牛ロースのしゃぶしゃぶ【一品{add_menu1}】：{menu1_num}個／{add_menu1_total}円<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;大更ホルモン鍋【一品{add_menu2}】：{menu2_num}個／{add_menu2_total}円<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;岩手県産牛の串焼き【一品{add_menu3}】：{menu3_num}個／{add_menu3_total}円<br>
    二次会：{nijikai_plan}【一人{nijikai_money}】：{nijikai_num}人／{nijikaitotal}円<br>
    ------------------------------------------------------------------------------------------------------<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;合計金額：{Banquettotal}円<br><br>
    〖早割〗<br>
    ------------------------------------------------------------------------------------------------------<br>
    60日前にご予約の方は、10％割引<br>
    90日前にご予約の方は、15％割引となります<br>
    予約はお早めに！<br>
    -------------------------------------------------------------------------------------------------------<br><br>
    ご予約はホームページから！<br>
    URL:<a href="https://8mantai.jp/">八幡平ハイツホームページ</a>
    
    </p>
    
    '''
    
    # メールメッセージの準備
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'html'))
    
    msg['Subject'] = '見積もり確認メール'
    msg['From'] = ID
    msg['To'] = email
    
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(ID, PASS)
    
    server.send_message(msg)
    server.quit()
    
    
import os
import json

def stay_estimate_data(name, email, numAdult, numChild, numStay, room, dinner,
                       Adultplan, Childplan, checkin_option, bedrockButh_option, 
                       peterAdult_option, peterChild_option, parkAdult_option, 
                       parkChild_option, tennis_option, hotSpringRental_option, 
                       dogone_option,numdog,dogoneSpa, quotationtotal):

    # **リストの長さをチェック**
    list_data = [numAdult, numChild, room, dinner, numStay, Adultplan, Childplan, checkin_option, 
                 bedrockButh_option, peterAdult_option, peterChild_option, parkAdult_option, 
                 parkChild_option, tennis_option, hotSpringRental_option, dogone_option,numdog,dogoneSpa,quotationtotal]
    
    if len(set(map(len, list_data))) != 1:
        raise ValueError("リストの長さが一致していません")

    # **相対パスで保存フォルダを指定**
    base_path = './Quote_folder/Stay_file'
    os.makedirs(base_path, exist_ok=True)  # **フォルダがなければ作成**

    # **インデックス管理ファイル**
    index_file = f'{base_path}/index.txt'
    file_index = 1

    if os.path.exists(index_file):
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                existing_indices = [int(line.strip()) for line in f.readlines()]
                if existing_indices:
                    file_index = max(existing_indices) + 1
        except ValueError:
            pass  # ファイルが壊れていた場合は 1 からスタート

    # **各リストの要素ごとに個別ファイルを作成**
    for i in range(len(numAdult)):  # すべてのリストは同じ長さ

        estimate_data = {
            '見積もり': {
                '氏名': name,
                'メール': email,
                '大人数': numAdult[i],
                '子供数': numChild[i],
                '部屋種類': room[i],
                '夕食': dinner[i],
                '泊数': numStay[i],
                '大人プラン': Adultplan[i],
                '子供プラン': Childplan[i],
                '土日祝': checkin_option[i],
                '岩盤浴': bedrockButh_option[i],
                'パターゴルフ大人': peterAdult_option[i],
                'パターゴルフ子供': peterChild_option[i],
                'パークゴルフ大人': parkAdult_option[i],
                'パークゴルフ子供': parkChild_option[i],
                'テニス': tennis_option[i],
                '貸し切り風呂': hotSpringRental_option[i],
                'ドックわん': dogone_option[i],
                '匹': dogone_option[i],
                'ドックスパ': dogone_option[i],
                '合計金額': quotationtotal[i],
            }
        }

        filename = f'{base_path}/estimate_{file_index + i}.json'

        # **既存ファイルとの重複チェック**
        for j in range(1, file_index + i):
            existing_filename = f'{base_path}/estimate_{j}.json'
            if os.path.exists(existing_filename):
                try:
                    with open(existing_filename, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                    if existing_data == estimate_data:
                        print(f'同じ内容の見積もりがすでに存在します: {existing_filename}')
                        return False  # **同じ内容なら保存しない**
                except (json.JSONDecodeError, FileNotFoundError):
                    print(f"ファイル {existing_filename} の読み込みに失敗しました。スキップします。")

        # **ファイルを保存**
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(estimate_data, f, indent=2, ensure_ascii=False)
            print(f'見積もりファイル {filename} を保存しました。')

            # **次のインデックス番号を記録**
            with open(index_file, 'a', encoding='utf-8') as f:
                f.write(f"{file_index + i}\n")

        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return False  # **エラー発生時は False を返す**

    return True  # **正常に処理が完了したら True を返す**

import os
import json

def Banquet_estimate_data(name, email, all_num, coursename, coursemoney, staynum, 
                          roomgrade1, roomgrade2, roomgrade1num, roomgrade2num, 
                          nominum, nomitime, add_menu1, add_menu2, add_menu3, 
                          menu1_num, menu2_num, menu3_num, nijikai_plan, nijikai_num, 
                          nijikai_money, staymoney, nostaymoney, nomitotal, nijikaitotal, 
                          roomgrade1total, roomgrade2total, add_menu1_total, 
                          add_menu2_total, add_menu3_total, Banquettotal):
    
    # 型チェック（数値系の変数が適切か確認）
    numeric_vars = [coursemoney, nijikai_money, staymoney, nostaymoney, nomitotal, 
                    nijikaitotal, roomgrade1total, roomgrade2total, 
                    add_menu1_total, add_menu2_total, add_menu3_total, Banquettotal]

    if not all(isinstance(var, (int, float)) for var in numeric_vars):
        raise ValueError("金額に関する変数はすべて数値（int または float）である必要があります。")

    # 見積もりデータを辞書として作成
    estimate_data = {
        '見積もり': {
            '氏名': name,
            'メール': email,
            '全体人数': all_num,
            'コース名': coursename,
            'コース料金': coursemoney,
            '宿泊人数': staynum,
            '宿泊者料金合計': staymoney,
            '非宿泊者料金合計': nostaymoney,
            'グレード1': roomgrade1,
            'グレード2': roomgrade2,
            'グレード1人数': roomgrade1num,
            'グレード2人数': roomgrade2num,
            'グレード1の部屋料金合計': roomgrade1total,
            'グレード2の部屋料金合計': roomgrade2total,
            '飲み放題の人数': nominum,
            '飲み放題時間': nomitime,
            '追加料理1': add_menu1,
            '追加料理2': add_menu2,
            '追加料理3': add_menu3,
            '追加料理1の数量': menu1_num,
            '追加料理2の数量': menu2_num,
            '追加料理3の数量': menu3_num,
            '追加料理1の合計金額': add_menu1_total,
            '追加料理2の合計金額': add_menu2_total,
            '追加料理3の合計金額': add_menu3_total,
            '二次会プラン': nijikai_plan,
            '二次会の人数': nijikai_num,
            '二次会の料金': nijikai_money,
            '飲み放題合計': nomitotal,
            '二次会合計': nijikaitotal,
            '合計金額': Banquettotal,
        }
    }

    # 保存先のディレクトリ
    base_path = './Quote_folder/Banquet_file'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # インデックス管理用のファイル
    index_file = f'{base_path}/index.txt'

    # インデックス番号の取得
    # インデックス番号の取得
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:  # 空でない場合
                file_index = int(content)
            else:  # 空の場合
                file_index = 1
    else:
        file_index = 1  # 初期値


    # すでに同じ内容のファイルが存在するかチェック
    for i in range(1, file_index):
        existing_filename = f'{base_path}/estimate_{i}.json'
        if os.path.exists(existing_filename):
            with open(existing_filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
                if existing_data == estimate_data:
                    print(f'同じ内容の見積もりがすでに存在します: {existing_filename}')
                    return

    # 新しいファイル名を生成
    filename = f'{base_path}/estimate_{file_index}.json'

    # 見積もりデータをJSONファイルとして保存
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(estimate_data, f, indent=2, ensure_ascii=False)
        print(f'見積もりファイル {filename} を保存しました。')

        # **次のインデックス番号を記録**
        file_index += 1
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"{file_index}\n")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False  # **エラー発生時は False を返す**

    return True  # **正常に処理が完了したら True を返す**