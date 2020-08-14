from Currency_Converter import *
import win10toast
toaster = win10toast.ToastNotifier()

if float(rate) > 94:
    toaster.show_toast('Current rate is:' + rate)
