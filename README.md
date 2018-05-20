# KLXB airport screening

## Description

Objection detection based on Baidu EasyDL.

## Usage

### H5 DEMO

<http://t.cn/R3TgfBt> 

### Python SDK

```
>>> from SSD import *
>>> ak = 'MyAccessToken'
>>> sk = 'MySecrectToken'
>>> sccess_token=get_access_token(ak, sk)
>>> b64_image = image_to_base64('1.jpg')
>>> result = screening_analysis(access_token, image=b64_image, threshold=0.3)
```

Example output:

```json
{
    'log_id': 8442232682833594486, 
    'results': [
        {
            'location': {'height': 172, 'left': 147, 'top': 114, 'width': 363}, 'name': 'pistol', 'score': 0.9317824244499207}, 
        {
            'location': {'height': 58, 'left': 537, 'top': 216, 'width': 54}, 'name': 'zipper', 'score': 0.5975794792175293}, 
        {
            'location': {'height': 63, 'left': 35, 'top': 192, 'width': 46}, 'name': 'zipper', 'score': 0.3447454571723938}, 
        {
            'location': {'height': 186, 'left': 237, 'top': 234, 'width': 232}, 'name': 'board', 'score': 0.3417820632457733}, 
        {
            'location': {'height': 104, 'left': 19, 'top': 174, 'width': 91}, 'name': 'zipper', 'score': 0.30391350388526917}
    ]
}
```



## 描述

基于百度 EasyDL 的安检机物体检测。

在机场、火车站安检系统中，往往需要人工识别安检机扫描显示的行李箱内物体

安检人员需要专门的训练来学习识别安检机显示的物体，这种专门训练和训练机器学习模型非常相似。计算机视觉技术能取代专门看显示器的安检人员

故考虑训练物体检测模型，辅助或代替安检人员识别物体，加快安检速度，解放人力资源

因为安检机数据多为保密数据，很难得到，故考虑用 X 射线扫描物体作为训练数据，安检机的原理部分基于 X 射线，所以 X 射线下训练出来的模型也能适用在实际安检环境中（可能需要稍微调整）

数据集中的 X 射线扫描数据包含——300～400张左轮手枪、50～100张手枪、1500～2000张各类小刀、500～1000张飞镖、40～60张易拉罐、各类杂物各几十张等等。

## 使用方法

### 体验 H5

<http://t.cn/R3TgfBt> 

![image-20180520093859832](https://ws3.sinaimg.cn/large/006tKfTcgy1frhk2z925cj30oi0l8k4l.jpg)

### Python SDK

#### 接口描述

 基于自定义训练出的物体检测模型，实现个性化图像识别。API 封装为 Python SDK。

#### 调用方式

见 `SSD.py` 中 `main()` 的例子

#### 返回值说明

![返回说明](https://ws4.sinaimg.cn/large/006tKfTcgy1frhi4xeclgj30uy0n8dj7.jpg)