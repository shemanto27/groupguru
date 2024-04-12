import flet as ft
import pyautogui
import time

def main(page: ft.Page):
    page.title = "GroupGuru: Your Social Media Group Manager!"
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = "#f2edd2"
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        
    }


    Title = ft.Text("GroupGuru: Your Social Media Group Manager!", font_family="Kanit")
    guru_image = ft.Image(src="Guru.jpg", width="150px", height="150px")  # Placeholder image source, adjust as needed
    
    groups = []
    txt = ft.Text("")

    def link_add(e):
        group_links = Group_links.value.split('\n')
        group_links = [link.strip() for link in group_links if link.strip()]
        
        # Append the links to the groups list
        groups.extend(group_links)
        print(groups)
        time.sleep(5)
        pyautogui.hotkey("ctrl" , "t")

        for i in range(len(groups)):
            link = groups[i]
            pyautogui.typewrite(link)
            pyautogui.typewrite('\n')

            print("Waiting for 45 seconds\n")
            time.sleep(10)

            pyautogui.typewrite('p')
            time.sleep(4)
            print("Writing post\n")
            pyautogui.typewrite(Contents.value)
            time.sleep(4)

            axis = pyautogui.locateCenterOnScreen("post.png")

            pyautogui.moveTo(axis)
            pyautogui.click(button='left')

            time.sleep(4)

            pyautogui.write(['f6'])
            time.sleep(1)
        groups.clear()
        txt.value.append("Task Completed Successfully!")


        
        page.update()

    Group_links = ft.TextField(label="ADD Group links", multiline = True,)
    Contents = ft.TextField(label="Write your post here", multiline = True,)
    submit_button = ft.ElevatedButton(text="Guru!Plz Start Posting🙏",on_click=link_add)
    


    page.add(
        guru_image,
        Title,
        Contents,
        Group_links,
        submit_button,
        txt
    )


ft.app(target=main)    