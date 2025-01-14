<?php
// channel  https://t.me/netcopy
// website https://netcopy.ir
ob_start();
error_reporting(0);
define('API_KEY', "666666666:AAFUfdxj5OQJ7OrgF2cIesTHNEaAo0oJGuc");// توکن
$channel = 'https://t.me/TESTGOLDNERKH';//---- ایدی کانال
$admin =https://t.me/mohammadmahdiahm; ///---- ایدی ادمین
function bot($method, $datas = []) {
    $url = "https://api.telegram.org/bot" . API_KEY . "/" . $method;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $datas);
    $res = curl_exec($ch);
    if (curl_error($ch)) {
        var_dump(curl_error($ch));
    } else {
        return json_decode($res);
    }
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
function SendMessage($chat_id, $text, $mode = null, $reply=null, $keyboard = null) {
    bot('SendMessage', ['chat_id' => $chat_id, 'text' => $text, 'parse_mode' => $mode, 'reply_to_message_id' => $reply, 'reply_markup' => $keyboard]);
}
function SendPhoto($chatid, $photo, $caption = null, $keyboard = null) {
    bot('SendPhoto', ['chat_id' => $chatid, 'photo' => $photo, 'caption' => $caption, 'parse_mode' => 'HTML',	'reply_markup' => $keyboard]);
}
function EditMsg1($chatid, $msgid, $text, $keyboard = null) {
    bot('EditMessageText', ['chat_id' => $chatid, 'message_id' => $msgid, 'text' => $text, 'reply_markup' => $keyboard]);
}
function EditMsg($chat_id, $text, $mode, $msg_id, $keyboard = null) {
    bot('EditMessageText', ['chat_id' => $chat_id, 'message_id' => $msg_id, 'text' => $text, 'parse_mode' => $mode, 'reply_markup' => $keyboard]);
}
function Forward($chat_id, $from_id, $massege_id) {
    bot('ForwardMessage', ['chat_id' => $chat_id, 'from_chat_id' => $from_id, 'message_id' => $massege_id]);
}
function objectToArrays($object) {
    if (!is_object($object) && !is_array($object)) {
        return $object;
    }
    if (is_object($object)) {
        $object = get_object_vars($object);
    }
    return array_map("objectToArrays", $object);
}
// [ Variables section ] . [ end functions , start Variables ]
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$chat_id = $message->chat->id;
$text = $message->text;
$message_id = $update->message->message_id;
$from_id = $message->from->id;
$name = $message->from->first_name;
$lastname = $message->from->last_name;
$username = $message->from->username;
$data = $update->callback_query->data;
$dataa = explode('|', $data); 
$chatid = $update->callback_query->message->chat->id;
$fromid = $update->callback_query->from->id;
$messageid = $update->callback_query->message->message_id;
$photo = $update->message->photo;
$now = date('h:i:s');

if (!is_dir("data")) {
    mkdir("data");
}

$user = json_decode(file_get_contents("data/user.json"), true);
$alluser = $user['users'];
$userinfo = json_decode(file_get_contents("data/data.json"), true);
$ban = $userinfo[$from_id]['ban'];
$step = $userinfo[$from_id]['step'];
// channel  https://t.me/netcopy
// website https://netcopy.ir
$get = json_decode(file_get_contents("https://api.telegram.org/bot" . API_KEY . "/getChatMember?chat_id=$channel&user_id=$from_id"), true);
$rank = $get['result']['status'];
// channel  https://t.me/netcopy
// website https://netcopy.ir
// [ end Force/Rank channel ] . [ start keyboards ]
$start = json_encode(['resize_keyboard' => true, 'inline_keyboard' => [[['text' => "دریافت ارز کشوری", 'callback_data' => "Country"]], [['text' => " راهنمای استفاده", 'callback_data' => "help"]], [['text' => "درباره ما", 'callback_data' => "us"]], ]]);
$back1 = json_encode(['resize_keyboard' => true, 'inline_keyboard' => [[['text' => "بازگشت", 'callback_data' => "back1"]], ]]);
$panel = json_encode(['keyboard' => [[['text' => "آمار"]], [['text' => "فروارد همگانی"], ['text' => "ارسال همگانی"]], [['text' => "حذف مسدود کاربر"], ['text' => "مسدود کاربر"]], ], 'resize_keyboard' => true]);
$arz=json_decode(file_get_contents("https://kashanaki.ir/we/arz/arz.php"),true);
$yoro=$arz['0']['price'];
$emarat=$arz['1']['price'];
$swead=$arz['2']['price'];
$norway=$arz['3']['price'];
$iraq=$arz['4']['price'];
$swit=$arz['5']['price'];
$armanestan=$arz['6']['price'];
$gorgea=$arz['7']['price'];
$pakestan=$arz['8']['price'];
$soudi=$arz['9']['price'];
$russia=$arz['10']['price'];
$india=$arz['11']['price'];
$kwait=$arz['12']['price'];
$astulia=$arz['13']['price'];
$oman=$arz['14']['price'];
$qatar=$arz['15']['price'];
$kanada=$arz['16']['price'];
$tailand=$arz['17']['price'];
$turkye=$arz['18']['price'];
$england=$arz['19']['price'];
$hong=$arz['20']['price'];
$azarbayjan=$arz['21']['price'];
$malezy=$arz['22']['price'];
$danmark=$arz['23']['price'];
$newzland=$arz['24']['price'];
$china=$arz['25']['price'];
$japan=$arz['26']['price'];
$bahrin=$arz['27']['price'];
$souria=$arz['28']['price'];
$dolar=$arz['29']['price'];
$talaa=json_decode(file_get_contents("https://kashanaki.ir/we/arz/tala.php"),true);
$tala=$talaa['4']['price'];
$nogre=$talaa['5']['price'];
$emami=$talaa['0']['price'];
$nim=$talaa['1']['price'];
$rob=$talaa['2']['price'];
$geram=$talaa['3']['price'];
$bahar=$talaa['6']['price'];
if (!in_array($from_id, $user["users"])) {
    $user["users"][] = "$from_id";
    $user = json_encode($user, true);
    file_put_contents("data/user.json", $user);
    $userinfo[$from_id]['step'] = "none";
    $userinfo[$from_id]['ban'] = "false";
    file_put_contents("data/data.json", json_encode($userinfo));
}
if ($ban == 'true') {
    exit();
}
if ($rank == 'left') {
    SendMessage($chat_id, "■ برای استفاده از ربات و همچنین حمایت از ما ابتدا وارد کانال\n● $channel\n■ سپس به ربات برگشته و /start را بزنید.", null, $message_id, json_encode(['KeyboardRemove' => [], 'remove_keyboard' => true]));
}
if ($text == "/start" and $rank != 'left') {
    $userinfo[$from_id]['step'] = "none";
    file_put_contents("data/data.json", json_encode($userinfo));
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"سلام $name عزیز 😃"
print("📶 به ربات نرخ لحظه ای طلا و ارز و... خوش آمدید")
print("🌟 به وسیله این ربات میتونی از اخرین قیمت های دلار و ارز های مختلف و کلی چیزای دیگه مطلع بشی")
print("🎈 برای شروع کافیه از دکمه های زیر استفاده کنی")
'parse_mode'=>"html",
'reply_markup'=>json_encode(['keyboard'=>[
    [['text'=>"💶 قیمت ارز"]],
    [['text'=>"🏵 قیمت طلا"],['text'=>"💰 قیمت سکه"]],
],
    'resize_keyboard'=>true,
    ])
]);
}
elseif($text=="💶 قیمت ارز"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"💵 قیمت ارز های کشور های مختلف:

🇪🇺 یورو : `$yoro`
------
🇺🇸 دلار : `$dolar`
------
🇦🇪درهم امارات  : `$emarat`
------
🇸🇪 کرون سوئد : `$swead`
------
🇳🇴 کرون نروژ : `$norway`
------
🇮🇶 دینار عراق : `$iraq`
------
🇨🇭فرانک سوئیس : `$swit`
------
🇦🇲 درام ارمنستان : `$armanestan`
------
🇬🇪لاری گرجستان : `$gorgea`
------
🇵🇰 روپیه پاکستان : `$pakestan`
------
🇷🇺 روبل روسیه : `$russia`
------
🇮🇳 روپیه هندوستان : `$india`
------
🇰🇼 دینار کویت : `$kwait`
------
🇦🇺 دلار استرلیا : `$astulia`
------
🇴🇲 ریال عمان : `$oman`
------
🇶🇦 ریال قطر : `$qatar`
------
🇨🇦 دلار کانادا : `$kanada`
------
🇹🇭بات تایلند : `$tailand`
------
🇹🇷 لیر ترکیه : `$turkye`
------
🇬🇧 پوند انگلیس : `$england`
------
🇭🇰 دلار هنگ کنگ : `$hong`
------
🇦🇿 منات اذربایجان : `$azarbayjan`
------
🇲🇾رینگیت مالزی : `$malezy`
------
🇩🇰 کرون دانمارک : `$danmark`
------
🇳🇿 دلار نیوزلند : `$newzland`
------
🇨🇳 یوان چین : `$china`
------
🇯🇵 ین ژآپن : `$japan`
------
🇧🇭 دینار بحرین : `$bahrin`
------
🇸🇾 لیر سوریه : `$souria`
",
'parse_mode'=>"MARKDOWN",
'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>"🌟اشتراک ",'switch_inline_query'=>""]]],
    ])
    ]);
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
elseif($text=="🏵 قیمت طلا"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"🏵قیمت طلا و نقره به دلار :

🥇انس طلا : `$tala`
------
🥈انس نقره : `$nogre`
",
'parse_mode'=>"MARKDOWN",
'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>"🌟اشتراک ",'switch_inline_query'=>""]]],
    ])
    ]);
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
elseif($text=="💰 قیمت سکه"){
bot('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"🏅قیمت سکه به تومان :

💰سکه گرمی : `$geram`
------
💰ربع سکه : `$rob`
------
💰نیم سکه : `$nim`
------
💰سکه بهار آزادی :  `$bahar`
------
💰سکه امامی : `$emami`
",
'parse_mode'=>"MARKDOWN",
'reply_markup'=>json_encode(['inline_keyboard'=>[[['text'=>"🌟اشتراک ",'switch_inline_query'=>""]]],
    ])
    ]);
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
elseif($inline==""){
    bot('answerInlineQuery', [
        'inline_query_id' => $up['inline_query']['id'],
        'results' => json_encode([[
            'type' => 'article',
            'id' => base64_encode(rand(5,555)),
            'thumb_url'=>"https://r2f.ir/web/BgvOnAb4.jpg",
            'title' => "ارسال نرخ ارز",
            'description'=>"ارسال نرخ ارز به این چت",
            'input_message_content'=>[
            'parse_mode' => 'html', 
            'message_text' => "$currency"],
'reply_markup'=>[
'inline_keyboard'=>[[["text"=>"🔹ورود به ربات"]],[["text"=>"🌟اشتراک",'switch_inline_query'=>""]]]]
         ],[
            'type' => 'article',
            'id' => base64_encode(rand(5,555)),
           'thumb_url'=>"https://r2f.ir/web/BgvOnAb4.jpg",
            'title' => "ارسال نرخ طلا",
            'description'=>"ارسال نرخ طلا به این چت",
            'input_message_content'=>[
            'parse_mode' => 'html', 
            'message_text' => "$gold"],
'reply_markup'=>[
'inline_keyboard'=>[[["text"=>"🔹ورود به ربات",'url'=>"https://t.me/oj_arzbot"]],[["text"=>"🌟اشتراک",'switch_inline_query'=>""]]]]
        ],[
            'type' => 'article',
            'id' => base64_encode(rand(5,555)),
            'thumb_url'=>"https://r2f.ir/web/BgvOnAb4.jpg",
            'title' => "ارسال نرخ سکه",
            'description'=>"ارسال نرخ سکه به این چت",
            'input_message_content'=>[
            'parse_mode' => 'html', 
            'message_text' => "$coin"],
'reply_markup'=>[
'inline_keyboard'=>[[["text"=>"🔹ورود به ربات",'url'=>"https://t.me/oj_arzbot"]],[["text"=>"🌟اشتراک",'switch_inline_query'=>""]]]]]
        ])
        ]);
}
if ($text == 'oj' or $text == '↜بازگشت') {
    if ($from_id == $admin) {
        $userinfo[$from_id]['step'] = "none";
        file_put_contents("data/data.json", json_encode($userinfo));
        SendMessage($chat_id, " به پنل مدیریت خوش آمدید", 'MarkDown', $message_id, $panel);
    }
}
if ($text == 'آمار' and $from_id == $admin) {
    $mmemcount = count($user['users']) - 1;
    SendMessage($chat_id, "■ تعداد کل اعضای ربات : *$mmemcount*", 'MarkDown', $message_id);
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
if ($text == 'ارسال همگانی' and $from_id == $admin) {
    $userinfo[$from_id]['step'] = "s2all";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ پیام مورد نظر را ارسال کنید", 'MarkDown', $message_id, $back_panel);
}
if ($step == "s2all") {
    $userinfo[$from_id]['step'] = "none";
    file_put_contents("data/data.json", json_encode($userinfo));
    while ($z <= count($alluser)) {
        $z++;
        SendMessage($alluser[$z - 1], $text);
    }
    SendMessage($chat_id, "■ پیام به تمامی اعضا ارسال شد", 'MarkDown', $message_id, $panel);
}
if ($text == 'فروارد همگانی' and $from_id == $admin) {
    $userinfo[$from_id]['step'] = "f2all";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ پیام مورد نظر را فروارد کنید", 'MarkDown', $message_id, $back_panel);
}
if ($step == "f2all") {
    $userinfo[$from_id]['step'] = "none";
    file_put_contents("data/data.json", json_encode($userinfo));
    while ($z <= count($alluser)) {
        $z++;
        Forward($alluser[$z - 1], $chat_id, $message_id);
    }
    SendMessage($chat_id, "■ پیام به تمامی اعضا فروارد شد", 'MarkDown', $message_id, $panel);
}
//------------------------------------------------------------------------------
if ($text == 'مسدود کاربر' and $from_id == $admin) {
    $userinfo[$from_id]['step'] = "ban";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ آیدی کاربر جهت محروم شدن از ربات را ارسال کنید", 'MarkDown', $message_id, $back_panel);
}
if ($step == "ban") {
    $userinfo[$from_id]['step'] = "none";
    $userinfo[$text]['ban'] = "true";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ کاربر `$text` از ربات مسدود شد!", 'MarkDown', $message_id, $panel);
}
if ($text == 'حذف مسدود کاربر' and $from_id == $admin) {
    $userinfo[$from_id]['step'] = "unban";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ آیدی کاربر جهت خارج کردن از محرومیت ربات را ارسال کنید", 'MarkDown', $message_id, $back_panel);
}
if ($step == "unban") {
    $userinfo[$from_id]['step'] = "none";
    $userinfo[$text]['ban'] = "false";
    file_put_contents("data/data.json", json_encode($userinfo));
    SendMessage($chat_id, "■ کاربر `$text` از مسدودیت خارج گردید", 'MarkDown', $message_id, $panel);
}
// channel  https://t.me/netcopy
// website https://netcopy.ir
