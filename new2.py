import tkinter
from datetime import datetime
from tkinter import ttk
import tkinter.messagebox
root = tkinter.Tk()
root.title("주조 실적 다운로드")
root.geometry('250x320')
disv = 25
starty = 30

label_customer = tkinter.Label(root, text = "**품종코드**")
label_customer.place(x=10, y=10)


combo_customer = ttk.Combobox(root, values=["SCG 1202005", "Cavagna 1202010", "Tai Peng Valve 1203388", "Hakudo 1203421", "Alconix 1201215", "G.KENT 1203052", "Hwaguan 1203080", "OMEGA 1202538", "TSM 1202725", "SEMA 1201134", "William Jacks 1203462", "KASH 1203551", "TSM FOUNDRY 1203645", "YIH SHAN 1202432", "GRAND GAS 1202785", "WU FENG 1200701", "Ing Shin 1202685"],width=20)
combo_customer.place(x=10, y=starty)

label_date = tkinter.Label(root, text = "**기간**")
label_date.place(x=10, y=starty+disv)

ent_date = tkinter.Entry(root, width = 15)
ent_date.place(x=10, y=starty+disv*2)
ent_date.insert(tkinter.END, "시작월")

ent_date2 = tkinter.Entry(root, width = 15)
ent_date2.place(x=120, y=starty+disv*2)
ent_date2.insert(tkinter.END, "종료월")


def btncmd_report():
    import win32com.client
    sap_gui_obj = win32com.client.GetObject("SAPGUI")
    application = sap_gui_obj.GetScriptingEngine
    connection = application.children(application.connections.count - 1)
    session = connection.children(0)

    customer = combo_customer.get()
    customer = customer[len(customer) - 7:len(customer)]
    start = ent_date.get()
    end = ent_date.get()
    product = ent_product.get()

    session.findById("wnd[0]/tbar[0]/okcd").text = "/n zcor093203"
    session.findById("wnd[0]").sendVKey(0)
    session.findById("wnd[0]/usr/txtS_PERIO-LOW").text = start
    session.findById("wnd[0]/usr/txtS_PERIO-HIGH").text = end
    session.findById("wnd[0]/usr/ctxtS_VKORG-LOW").text = ""
    session.findById("wnd[0]/usr/ctxtS_SPART-LOW").text = "00"
    session.findById("wnd[0]/usr/ctxtS_SPART-HIGH").text = "99"
    session.findById("wnd[0]/usr/ctxtS_VTWEG-LOW").text = "50"
    session.findById("wnd[0]/usr/ctxtS_KNDNR-LOW").text = customer
    session.findById("wnd[0]/usr/ctxtS_ARTNR-LOW").text = product
    session.findById("wnd[0]").sendVKey(8)
    session.findById("wnd[0]/tbar[1]/btn[32]").press()
    session.findById(        "wnd[1]/usr/tabsG_TS_ALV/tabpALV_M_R1/ssubSUB_DYN0510:SAPLSKBH:0620/cntlCONTAINER1_LAYO/shellcont/shell").selectAll()
    session.findById("wnd[1]/usr/tabsG_TS_ALV/tabpALV_M_R1/ssubSUB_DYN0510:SAPLSKBH:0620/btnAPP_WL_SING").press()
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
    session.findById("wnd[0]/mbar/menu[0]/menu[3]/menu[2]").select()
    session.findById("wnd[1]/usr/sub:SAPLSPO5:0201/radSPOPLI-SELFLAG[1,0]").select()
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
    session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = f'{start}_{end}_{customer}_{today}_report.xls'
    session.findById("wnd[1]/tbar[0]/btn[0]").press()
btn_POstock = tkinter.Button(root, text = "엑셀 저장하기", command=btncmd_report, width = 30, height= 5)
btn_POstock.place(x=10, y=starty+disv*4)


root.mainloop()