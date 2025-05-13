import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def links(name: str, ref: str):
    return rx.link(
        rx.text(
            name,
            class_name="text-white transition delay-100 duration-500 ease-in-out hover:text-white hover:underline decoration-amber-500 hover:scale-110"
        ),
        href=f"{ref}",
        class_name="py-[0.5em]"
    )


def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(  # logo
                        src="/logo.png",
                        border_radius="25%",
                        class_name="justify-center items-center h-[2em]",
                    ),
                    rx.heading(
                        "IT Com", class_name="text-white dark:text-white"
                    ),
                ),
                rx.hstack(
                    links("Home", "#home"),
                    links("About Us", "#about"),
                    links("Organization", "#organization"),
                    rx.color_mode.button(
                        class_name="transition delay-100 duration-500 ease-in-out hover:scale-110 hover:outline"
                    ),
                    spacing="4",
                    class_name="justify-end items-center justify-center",
                ),
                class_name="justify-between"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(  # logo
                        src="/logo.png",
                        border_radius="25%",
                        class_name="justify-center items-center h-[2em]",
                    ),
                    rx.heading(
                        "IT Com", class_name="text-white dark:text-white"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        links("Home", "#home"),
                        links("About Us", "#about"),
                        links("Organization", "#organization"),
                    ),
                    justify="end",

                ),
                justify="between",
                align_items="center",
            ),
        ),
        class_name=(
            "bg-blue-500 shadow-xl fixed z-40 w-full",
            "px-4 py-2"
        )
    )


def header():
    return rx.flex(
        rx.container(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Welcome To",
                        class_name="font-bold text-white dark:text-white text-[2em] md:text-[3em]"
                    ),
                    rx.heading(
                        "Information and Technology Community",
                        font_family="Neue Machina",
                        class_name="text-[2em] text-white dark:text-white text-left md:text-[2.5em] md:pt-[1vh] "

                    )
                ),
                rx.text(
                    "IT Com (Information and Technology Community) Merupakan salah satu dari 4 komunitas yang berada dibawah naungan Himpunan Mahasiswa Elektro Universitas Jember dimana komunitas ini mengumpulkan mahasiswa-mahasiswa yang ingin belajar mengenai bidang IT.",
                    size={"base": "1", "md": "4"},
                    as_="p",
                    class_name="text-white dark:text-white text-left md:text-left"

                ),
                rx.text(
                    "Gabung di komunitas, ikuti event kami, dan jadilah bagian dari kami!",
                    size={"base": "3", "md": "4"},
                    font_family="Poppins",
                    class_name="py-4 text-white dark:text-white text-justify md:text-left"
                ),
                rx.hstack(
                    rx.link(
                        rx.button("Join Now!"),
                        href="https://forms.gle/PNJ7dDibmow8sFUNA",
                        is_external=True,
                    ),
                    class_name="w-full justify-end md:pr-[10vw]"
                ),
                spacing="5",
                class_name="min-h-screen justify-center items-start px-8"

            ),
            size="4",
            class_name="bg-gray-900/70 w-full"
        ),
        class_name="bg-header bg-fixed h-screen w-full",
        id='home'
    )


def abautUs():
    return rx.box(
        rx.container(
            rx.flex(
                rx.heading(
                    "Di IT Com Memperlajari Apa Saja ?",
                    class_name="text-xl md:text-4xl text-white dark:text-white"
                ),
                rx.grid(
                    rx.card(
                        rx.image(
                            '/ui-ux.png',
                            class_name="h-[10dvh] md:h-[25dvh] justify-self-center"
                        ),
                        class_name="h-[13dvh] w-full md:w-auto md:h-[30dvh] row-span-3 justify-self-center self-center mr-4 py-4 shadow-xl text-white dark:text-white"
                    ),
                    rx.heading(
                        "UI/UX",
                        class_name="self-center col-span-2 text-[1em] md:text-[1.5em] text-white dark:text-white",
                    ),
                    rx.text(
                        "User Interface / User Experience atau sering di sebut UI / UX adalah Sebuah Proses membuat design visual dari sebuah produk digital yang dapat memberikan sebuah pengalaman pada Pengguna atau Usernya.",
                        class_name="col-span-2 row-span-2 self-start text-justify text-[0.7em] md:text-[1em] md:pb-[5dvh] text-white dark:text-white",
                    ),

                    rx.card(
                        rx.image(
                            '/html-css.png',
                            class_name="h-[10dvh] md:h-[25dvh] justify-self-center"
                        ),
                        class_name="h-[13dvh] w-full md:w-auto md:h-[30dvh] row-span-3 justify-self-center self-center mr-4 py-4 shadow-xl"
                    ),
                    rx.heading(
                        "HTML & CSS",
                        class_name="self-center col-span-2 text-[1em] md:text-[1.5em] text-white dark:text-white",
                    ),
                    rx.text(
                        "HTML adalah bahasa markup yang digunakan untuk menyusun dan menampilkan konten dalam sebuah halaman web. Sedangkan CSS di gunakan utuk membaut tampilan web lebih berwarna dan juga lebih indah.",
                        class_name="col-span-2 row-span-2 self-start text-justify text-[0.7em] md:text-[1em] md:pb-[5dvh] text-white dark:text-white",
                    ),

                    rx.card(
                        rx.image(
                            '/iot.png',
                            class_name="h-[10dvh] md:h-[25dvh] justify-self-center"
                        ),
                        class_name="h-[13dvh] w-full md:w-auto md:h-[30dvh] row-span-3 justify-self-center self-center mr-4 py-4 shadow-xl text-white dark:text-white"
                    ),
                    rx.heading(
                        "Internet of Things",
                        class_name="self-center col-span-2 text-[1em] md:text-[1.5em] text-white dark:text-white",
                    ),
                    rx.text(
                        "Internet of Things (IoT) adalah konsep yang memungkinkan benda-benda atau objek fisik (seperti sensor, perangkat, mesin, kendaraan, dan lain-lain) terhubung ke internet dan saling berkomunikasi serta bertukar data tanpa intervensi manusia.",
                        class_name="col-span-2 row-span-2 self-start text-justify text-[0.7em] md:text-[1em] md:pb-[5dvh] text-white dark:text-white",
                    ),

                    class_name="grid-cols-3 grid-flow-row gap-1 mx-[10dvw] md:my-[5dvh]"
                ),
                class_name="md:h-screen w-full justify-start items-center flex-col py-[5dvh]",
            ),
            size='4',
        ),
        class_name="bg-gray-900 md:pb-[15dvh]",
        id="about"
    )


def visiMisi():
    return rx.flex(
        rx.container(
            rx.vstack(
                rx.spacer(),
                rx.card(
                    rx.text(
                        "Visi",
                        font_family="Poppins",
                        class_name="py-4 text-xl sm:text-2xl lg:text-3xl text-white dark:text-white"
                    ),
                    rx.box(
                        rx.text(
                            "Menjadi wadah pengembangan teknologi informasi dan Menyediakan platform untuk berbagi ilmu dan pengalaman.",
                            font_family="Poppins",
                            class_name="text-sm sm:text-base md:text-lg px-4 py-2 text-white text-center"
                        ),
                    ),
                    variant="classic",
                    class_name="w-full max-w-screen-md outline outline-sky-500"
                ),
                rx.card(
                    rx.text(
                        "Misi",
                        font_family="Poppins",
                        class_name="py-4 text-xl sm:text-2xl lg:text-3xl text-white dark:text-white"
                    ),
                    rx.box(
                        rx.list.ordered(
                            rx.list.item(
                                rx.text(
                                    "Menyelenggarakan pelatihan secara berkala untuk meningkatkan keterampilan anggota dalam berbagai bidang teknologi informasi.",
                                    class_name="text-sm sm:text-base md:text-lg text-white dark:text-white"
                                )
                            ),
                            rx.list.item(
                                rx.text(
                                    "Membentuk forum diskusi dan kelompok belajar di mana anggota dapat berbagi pengetahuan dan pengalaman dalam teknologi informasi.",
                                    class_name="text-sm sm:text-base md:text-lg text-white dark:text-white"
                                )
                            ),
                            rx.list.item(
                                rx.text(
                                    "Menyusun nawala bulanan yang berisi panduan teknologi, pembaruan komunitas, serta rekomendasi materi pembelajaran.",
                                    class_name="text-sm sm:text-base md:text-lg text-white dark:text-white"
                                )
                            ),
                            class_name="px-4 py-2 text-center"
                        )
                    ),
                    variant="classic",
                    class_name="w-full max-w-screen-md outline outline-sky-500"
                ),
                rx.spacer(),
                spacing="6",
                class_name="min-h-[85dvh] items-center"
            ),
            size="4",
            class_name="bg-gray-900/70 w-full"
        ),
        class_name="bg-header-2 bg-fixed w-full justify-center items-center"
    )


def foto(*args):
    if not args:
        return rx.text("Tidak ada gambar")

    card_pertama = rx.card(
        rx.flex(
            rx.image(src=f"/{args[0]}", alt="Foto 1",
                     class_name="w-full max-w-xs h-auto"),
            align="center",
            justify="center",
        ),
        class_name="bg-white shadow-xl outline outline-sky-500 m-2"
    )

    cards_lainnya = [
        rx.card(
            rx.flex(
                rx.image(src=f"/{img}", alt=f"Foto {i+2}",  # +2 karena dimulai dari index 1
                         class_name="w-full max-w-xs h-auto"),
                align="center",
                justify="center",
            ),
            class_name="bg-white shadow-xl outline outline-sky-500 m-2"
        )
        for i, img in enumerate(args[1:])
    ]

    return rx.vstack(
        card_pertama,
        rx.hstack(
            *cards_lainnya,
            class_name="flex-wrap justify-center"  # biar wrap kalau sempit
        ) if cards_lainnya else rx.text(""),
        class_name="items-center w-full"
    )


def organisasi():
    return rx.flex(
        rx.vstack(
            foto("1.jpg", "2.jpg", "3.jpg"),
            foto("4.jpg", "5.jpg", "6.jpg"),
            foto("7.jpg", "8.jpg", "9.jpg"),
            foto("10.jpg", "11.jpg", "12.jpg", "13.jpg"),
            foto("14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg"),
            foto("19.jpg", "20.jpg", "21.jpg"),
            class_name="w-full items-center px-4 py-10 gap-6"
        ),
        class_name="bg-gray-900 w-full justify-center",
        id="organization"
    )


def index() -> rx.Component:
    return rx.flex(
        navbar(),
        header(),
        abautUs(),
        visiMisi(),
        organisasi(),
        # background_color=rx.color_mode_cond(
        #     light=rx.color("blue", 12), dark=rx.color("gray", 5)
        # ),
        justify="start",
        direction="column",
        class_name="h-screen w-full"
    )


app = rx.App(
    stylesheets=[
        "/styles.css",
        "https://fonts.google.com/specimen/Cal+Sans"
    ],


)
app.add_page(index)
