# Get user input
filename = input("File name: ")
new_filename = filename.lower()
# If gif or png or jpg or jpeg, print "image/type"
if '.gif' in new_filename:
    print("image/gif")
elif '.png' in new_filename:
    print("image/png")
elif '.jpg' in new_filename:
    print("image/jpeg")
elif '.jpeg' in new_filename:
    print("image/jpeg")
# If pdf or zip, print "application/type"
elif '.pdf' in new_filename:
    print("application/pdf")
elif '.zip' in new_filename:
    print("application/zip")
# If txt, print "text/plain"
elif '.txt' in new_filename:
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
