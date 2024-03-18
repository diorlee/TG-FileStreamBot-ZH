# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """
<i>👋 嗨，</i>{}\n
<i>我是 Telegram 文件流媒体机器人以及直链生成器</i>\n
<i>点击下方的 帮助 获取更多信息</i>\n
<i><u>警告 🚸</u></i>\n
<b>🔞 请勿分享色情内容，否则将导致您被永久封禁。</b>\n\n"""

        HELP_TEXT = """
<i>- 向我发送任何文件或来自 Telegram 的媒体。</i>
<i>- 我将提供一个外部直接下载链接！</i>
<i>- 享受极速的下载体验</i>
<u>🔸 警告 🚸</u>\n
<b>🔞 分享色情内容将导致您被永久封禁。</b>\n
<i>如需联系开发者或报告错误</i> <b>: <a href='https://t.me/baidugo'>[ 点击这里 ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ 我的名字：公共链接生成器</b>\n
<b>🔸版本：3.0.3.1</b>\n
<b>🔹最后更新时间：[ 18-Feb-22 ] 12:36 AM</b>
"""

        stream_msg_text ="""
<i><u>您的链接已生成！</u></i>\n
<b>📂 文件名：</b> <i>{}</i>\n
<b>📦 文件大小：</b> <i>{}</i>\n
<b>📥 下载：</b> <i>{}</i>\n
<b>🖥 观看：</b> <i>{}</i>"""

    class Test(object):
        START_TEXT = """
<i>👋 嗨，</i>{}\n
<i>我是 Telegram 文件流媒体机器人以及直链生成器</i>\n
<i>点击下方的 帮助 获取更多信息</i>\n
<i><u>警告 🚸</u></i>\n
<b>🔞 请勿分享色情内容，否则将导致您被永久封禁。</b>\n\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('帮助', callback_data='help'),
        InlineKeyboardButton('关于', callback_data='about'),
        InlineKeyboardButton('关闭', callback_data='close')
        ],
        [InlineKeyboardButton("📢 机器人频道", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('主页', callback_data='home'),
        InlineKeyboardButton('关于', callback_data='about'),
        InlineKeyboardButton('关闭', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 机器人频道", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('主页', callback_data='home'),
        InlineKeyboardButton('帮助', callback_data='help'),
        InlineKeyboardButton('关闭', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 机器人频道", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
