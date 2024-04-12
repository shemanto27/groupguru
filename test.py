import flet as ft  # Importing flet for creating the GUI
import pyautogui  # Importing pyautogui for automating mouse and keyboard interactions
import time       # Importing time for adding delays

def main(page: ft.Page):
    # Title and alignment settings
    page.title = "GroupGuru: Your Social Media Group Manager!"
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    Title = ft.Text("GroupGuru: Your Social Media Group Manager!")
    # Image of Guru
    guru_image = ft.Image(src="Guru.jpg", width="150px", height="150px")  # Placeholder image source, adjust as needed

    # Text Fields
    Group_links = ft.TextField(label="ADD Group links", width="80%", height="100px", multiline=True)
    Contents = ft.TextField(label="Write your post here", width="80%", height="200px", multiline=True)

    # Button
    submit_button = ft.ElevatedButton(text="Submit", width="50%", height="40px", on_click=link_add)

    # Text to display completion message
    txt = ft.Text("")


def link_add(e):
    # Your existing code for handling link submission
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


    # Add elements to the page
    page.add(
        guru_image,
        Title,  # Add Guru image
        Group_links,
        Contents,
        submit_button,
        txt
    )


ft.app(target=main)
