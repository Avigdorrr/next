
import file1
import file2


def main():

    g = file1.GreetingCard()
    g.greeting_msg()

    b = file2.BirthdayCard(sender_age=20)
    b.greeting_msg()


if __name__ == "__main__":
    main()