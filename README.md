# 病患分流系統
## 簡介
* 使用者使用時須先進行登入
* 本系統提供使用者設定緊急程度的總級數
* 每個病患都會有姓名、年齡、性別與緊急程度四個資料
* 每個病患會根據緊急程度存放於節點中
* 當所有資料編輯完後，給予該檔案一個編號，並以此為依據存檔
* 每個檔案皆會有其編號，所有的編號會另外儲存管理

## 系統概述
* <strong>本系統可製造不只一顆患者的資料樹，而每份患者文件存放一顆樹，也因此在一開始使用時使用者必須選擇要創建新的資料樹還是從原先的資料樹中擇一取出資料並編輯</strong>
* 提供帳密管理使用者確保安全性，執行過程將帳密存於<strong>二維陣列</strong>
* 針對不同區域、用途的病患資料樹文件，能夠使用不同編號區隔，而所有資料樹文件的編號將會存放於<strong>2-3樹</strong>中，並於結束時統一存檔管理
* 不論是新檔案還是舊檔案，都會有一棵<strong>標準二元樹</strong>來儲存個檔案中各層級的資料
* 各層級的資料中有<strong>鏈結串列</strong>將每個病患連起來
* 檢視單一檔案所有病患資料時，先將資料轉換成<strong>三維陣列</strong>，再透過<strong>heapq</strong>從層級小到大依序輸出
* 存檔時將帳密資料、編號列表、病患資料表用<strong>記事本儲存</strong>以利之後使用
* 部分方法使用<strong>視窗執行</strong>
* 部分方法使用<strong>堆疊、遞迴結構</strong>

## 技術列表
* 資列結構相關:
  * 二維陣列:讀取後的使用者帳密存在這裡
  * 三維陣列:印出所有內容的第一步就是將資料轉換成三維陣列 eg.[[[‘層級’, [病患資料]], [層級’, [病患資料]]…]
  * 標準二元樹與相關應用:層級數目相同的一顆節點樹
  * 鏈結串列與相關應用:同一層的的病患會用鏈結串列連起來
  * 2-3樹與相關應用:多個病患文件有著彼此不同編號，用2-3樹儲存所有編號，以此來做後續應用
  * 堆疊、遞迴:樹的建立過程與查找，或是印出資料的相關處理都會用到
  * Heapq:將儲存所有病患資料的陣列利用heapq從層級小到大依序排列輸出資料

* 其他:
  * 記事本文件讀取、編輯、儲存:患者資料文件、使用者帳密列表、所有文件編號的文件
  * 除錯、例外判斷:針對可能發生的邏輯錯誤以及使用者的惡意輸入進行防範
  * 視窗介面設計:部分輸入採用視窗進行，並利用提示資訊引導動作
  * 二元樹與鏈結串列的整合:在二元樹的每個節點中使用鏈結串列
  * 文件編譯方式:用特殊技術避免文件在加解碼過程使用不同方式造成的讀取錯誤
  * 視窗中事件偵測:對於關閉視窗、輸入內容判讀等進行相應動作
  * 輸入邏輯判斷:要求姓名輸入只能中英並規定長度、輸入的層級與年齡是否不合理
  * 結束完一份文件的編輯後，可以選擇開啟其他文件或創建文件再次使用，不需再登入
  * 鏈結串列的刪除與搜尋
  * 樹的搜尋
  * Heapq的應用
  * 使用者身分驗證:帳密系統
  * 節省算力:刪除、修改、與查詢前先判斷是否有病患資料存在，以及在輸入部分篩選掉過於不合理的內容，如過大的層級範圍、年齡
  * 多檔案撰寫，提升後續更改效率
  * 簡潔明瞭的提示字有效引導執行

## 檔案功能
<img width="709" height="358" alt="image" src="https://github.com/user-attachments/assets/eff8ef9c-43d9-4520-957d-becb9afb0d22" />

<img width="786" height="443" alt="image" src="https://github.com/user-attachments/assets/8a7f43f2-437f-4fa8-8646-78af02eea117" />

## 操作畫面

<img width="512" height="354" alt="image" src="https://github.com/user-attachments/assets/4eb677bc-9826-49d5-b2b0-5c0d6d9e6dc1" />
<img width="667" height="348" alt="image" src="https://github.com/user-attachments/assets/102f9bcd-0387-4e88-8607-b012e6410a3a" />
<img width="535" height="343" alt="image" src="https://github.com/user-attachments/assets/bf95cdf4-2036-40c3-85a0-b848dd3f5e95" />
<img width="563" height="319" alt="image" src="https://github.com/user-attachments/assets/4d36a37d-8d4a-41a3-b08c-27f53879ad34" />
<img width="409" height="355" alt="image" src="https://github.com/user-attachments/assets/48083aa7-ad14-4f69-9bc1-7279fabbf5b4" />
<img width="665" height="341" alt="image" src="https://github.com/user-attachments/assets/24e74ecb-242e-4187-890f-6340bca2635f" />
<img width="562" height="365" alt="image" src="https://github.com/user-attachments/assets/ff037b76-2013-4a13-8db0-fe001a9d4daf" />
<img width="678" height="418" alt="image" src="https://github.com/user-attachments/assets/a16b1b63-9a41-47d5-a89f-ab0939b97839" />
