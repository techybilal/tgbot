class Translation(object):
    START_TEXT = """Hey Welcome to Any File to Link Bot
<b>Please send me any direct download URL Link, i can upload to telegram as File/Video</b>
/help for more details.
              🎈 @URobots 🎈."""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "/help for Details"
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. Please use https://www.seedr.cc/ and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "📥 𝑫𝒐𝒘𝒏𝒍𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒆𝒂𝒔𝒆 𝑾𝒂𝒊𝒕 !!"
    UPLOAD_START = "📤 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 !!"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. Join : @URobots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nJoin : @URobots \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ 𝗖𝘂𝘀𝘁𝗼𝗺 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗰𝗹𝗲𝗮𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝗳𝘂𝗹𝗹𝘆."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ 𝗠𝗲𝗱𝗶𝗮 𝗰𝗹𝗲𝗮𝗿𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝗳𝘂𝗹𝗹𝘆."
    SAVED_RECVD_DOC_FILE = "✅ 𝘿𝙤𝙘𝙪𝙢𝙚𝙣𝙩 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
    CUSTOM_CAPTION_UL_FILE = "@URobots"
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: LifeTime
Expires on: 31/12/2040"""
    HELP_USER = """Hello i am Any File to Link Bot..
    
𝟏. 𝐒𝐞𝐧𝐝 𝐮𝐫𝐥 (𝐋𝐢𝐧𝐤|𝐍𝐞𝐰 𝐍𝐚𝐦𝐞 𝐰𝐢𝐭𝐡 𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧).
𝟐. 𝐒𝐞𝐧𝐝 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (𝐎𝐩𝐭𝐢𝐨𝐧𝐚𝐥).
𝟑. 𝐒𝐞𝐥𝐞𝐜𝐭 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧.
   𝐒𝐕𝐢𝐝𝐞𝐨 - 𝐆𝐢𝐯𝐞 𝐅𝐢𝐥𝐞 𝐚𝐬 𝐯𝐢𝐝𝐞𝐨 𝐰𝐢𝐭𝐡 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬
   𝐃𝐅𝐢𝐥𝐞  - 𝐆𝐢𝐯𝐞 𝐅𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬
   𝐕𝐢𝐝𝐞𝐨  - 𝐆𝐢𝐯𝐞 𝐅𝐢𝐥𝐞 𝐚𝐬 𝐯𝐢𝐝𝐞𝐨 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬
   𝐃𝐅𝐢𝐥𝐞  - 𝐆𝐢𝐯𝐞 𝐅𝐢𝐥𝐞 𝐰𝐢𝐭𝐡𝐨𝐮𝐭 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬
   
Join : @URobots"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @AnyFiletoLinkBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "𝗔𝗻𝗮𝗹𝘆𝘇𝗶𝗻𝗴 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 𝗳𝗶𝗹𝗲. ⚠️ 𝗧𝗵𝗶𝘀 𝗺𝗶𝗴𝗵𝘁 𝘁𝗮𝗸𝗲 𝘀𝗼𝗺𝗲 𝘁𝗶𝗺𝗲. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗯𝗲 𝗽𝗮𝘁𝗶𝗲𝗻𝘁. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists,"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
