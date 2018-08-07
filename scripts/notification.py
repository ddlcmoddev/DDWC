from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Monika",
              "I still love you [user]",
              icon_path="custom.ico",
              duration=5) 
toaster.show_toast("Monika",
              "come back to me",
              icon_path="custom.ico",
              duration=2) 
toaster.show_toast("Monika",
              "please",
              icon_path="custom.ico",
              duration=1)