import message

message.hello()
message.bye()

import message as msg # gives a another name

msg.hello()
msg.bye()

from message import hello,bye # Takes only of you determine functions

hello()
bye()

from message import * # Takes all functions

hello()
bye()

#help("modules") #it gives all modules in Python