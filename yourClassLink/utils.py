from smtplib import SMTP


def notify_new_university(name):
    my_email = "yourclasslink.auth@gmail.com"
    password = "syirdlcfvjppaeuj"
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="keenavasiloff@gmail.com",
                            msg=f"Subject:New University Request\n\nUniversity Name: {name}")
