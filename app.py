class Hello:
    def __init__(self, nama):
        self.nama = nama

    def greeting(self):
        print("Hello " + self.nama)


if __name__ == "__main__":
    app = Hello("budi")
    app.greeting()
