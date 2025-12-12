# every objects are executed here there might be classes on another file. 
from laptop import Laptop
from laptop import Computer
acer = Laptop("Acer", 16, 512)
acer.increase_ram(16)
acer.increasestorage(256)
acer.showsepcs()

dell = Computer("dell 303", 16, 1048, "Nvidia 5080 super")
dell.showsepcs()
from laptop import digitial
ludo = digitial ("pukas", 8, "3050 nvidia")
ludo.digitial()