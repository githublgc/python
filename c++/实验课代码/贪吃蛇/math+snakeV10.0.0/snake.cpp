#include "snake.h"
#include "ui_snake.h"
#include<qrect.h>
#include<qtimer.h>
#include<QKeyEvent>
#include<QDebug>
#include<QFont>
#include<QPixmap>
Snake::Snake(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Snake),blsRun(false),speed(500)
{
    ui->setupUi(this);
    this->setGeometry(QRect(600,300,1590,1610));
}

Snake::~Snake()
{
    delete ui;
}
void Snake::paintEvent(QPaintEvent *event){//update()或程序第一次启动时自动执行，用于画图
    QPainter painter(this);
    if(!blsRun){//只有blsRun为false时才需要初始化蛇
        InitSnake();//初始化蛇，此时蛇还没有画，只是初始化了矩形，没有显示
    }
    //画游戏背景
    //外墙
    painter.setPen(Qt::green);//设置画笔颜色
    painter.setBrush(Qt::white);//设置填充颜色
    painter.drawRect(15,15,660,660); //画矩形，相对于窗体的起点坐标（15，15），更新大小变成更大的660,660
    //内墙
    painter.setPen(Qt::gray);//设置画笔颜色
    painter.setBrush(Qt::gray);//设置填充颜色

    //painter.drawRect(20,20,250,250); //画矩形，相对于窗体的起点坐标（20，20），更新对应变大成大小650

    painter.drawPixmap(20,20,650,650,QPixmap(":/myIamge/image1/1.jpg"));//更新：导入图片1


    //画小格子，大小10*10
   /*painter.setPen(Qt::yellow);//设置画笔颜色
    for(int i=2;i<=27;i++){
        painter.drawLine(20,i*10,270,i*10);//画横线，270是根据坐标换算出来的
        painter.drawLine(i*10,20,i*10,270);//画竖线
    }
    //显示游戏开始、结束
*/


    QFont font1("Courier",24);
    painter.setFont(font1);
    painter.setPen(Qt::red);
    painter.setBrush(Qt::red);
    painter.drawText(40,150,sDisplay);
    //得分显示
    QFont font2("Courier",15);
    painter.setFont(font2);
    painter.setPen(Qt::red);
    painter.setBrush(Qt::black);
    painter.drawText(840,300,scoreLabel);//改变:颜色和位置，让最大化后的界面不显得太空，小界面也跟饱满
    painter.drawText(1140,300,QString::number(nScore));
    //画蛇
    painter.setPen(Qt::black);//设置画笔颜色

    painter.setBrush(Qt::yellow);//更新：设置填充颜色，换成黄色，对比度更鲜明
    painter.drawRect(SnakeHead);
    painter.drawPixmap(SnakeHead,QPixmap(":/myIamge/image/3.jpge"));//更新：给蛇头导入了图片3

    painter.drawRect(food);
    painter.drawPixmap(food,QPixmap(":/myIamge/image1/2.jpeg"));//更新：导入了图片二

    //图片有一点小。。。是白色底的香蕉，光标放到上面路径可看。



    painter.drawRects(&vSnakeRect[0],vSnakeRect.size());//画n个小方块
    if(blsOver)//游戏结束，停止计时器
        timer->stop();
}
void Snake::InitSnake(){
    nDirection=4;//更新起始方向：开始向右
    blsRun=true;
    blsOver=false;
    sDisplay="start";
    scoreLabel="goal";
    nScore=0;
    food=CreateRect();//创建食物
   // QRect rect(100,70,10,10);//蛇的初始位置
   // vSnakeRect=rect;//将矩形赋值给蛇

    vSnakeRect.resize(8);//初始化snake的长度是5_>8

    //利用一个for循环初始化vector
    for(int i=0;i<vSnakeRect.size();i++){
        QRect rect(100,70+10*i,10,10);//生成小方块，但是发现如果换成30，30大小的会出现碰到食物吃不到的问题，即便食物也改成30，30也不行
        vSnakeRect[vSnakeRect.size()-1-i]=rect;//小方块赋值到容器
    }
    SnakeHead=vSnakeRect.first();//指定蛇头位置
    timer=new QTimer(this);//设定计时器
    timer->start(speed);//计时器时间是0.5s
    connect(timer,SIGNAL(timeout()),SLOT(Snake_update()));//信号连接槽，发出信号的是timer，信号是timeout，执行的槽是Snake_update

}
void Snake::Snake_update(){
    sDisplay="";
    SnakeHead=vSnakeRect.first();//获取到蛇头
    IsEat();
    IsHit();
    //让数组移动，除了蛇头，后面的到前面的位置，因为蛇头是控制方向的
    for(int j=0;j<vSnakeRect.size()-1;j++){
        vSnakeRect[vSnakeRect.size()-1-j]=vSnakeRect[vSnakeRect.size()-2-j];
    }
    //下面我们要根据方向，来对蛇头小方块的移动方向进行调整
    switch(nDirection)
    {
    case 1:
        SnakeHead.setTop(SnakeHead.top()-10);
        SnakeHead.setBottom(SnakeHead.bottom()-10);
        break;
    case 2:
        SnakeHead.setTop(SnakeHead.top()+10);
        SnakeHead.setBottom(SnakeHead.bottom()+10);
        break;
    case 3:
        SnakeHead.setLeft(SnakeHead.left()-10);
        SnakeHead.setRight(SnakeHead.right()-10);
        break;
    case 4:
        SnakeHead.setLeft(SnakeHead.left()+10);
        SnakeHead.setRight(SnakeHead.right()+10);
    default:;


    }
    vSnakeRect[0]=SnakeHead;//第一个节点设置为蛇头位置
    if(SnakeHead.left()<20||SnakeHead.right()>670||SnakeHead.top()<20 || SnakeHead.bottom()>670){
        //更新：撞墙这块下和右也要对应改范围，注意要比650稍大一点，否则看上去的效果好像没到墙就停了
        sDisplay="游戏结束";
        blsOver=true;
    }

        update();//paintEvent更新
}
void Snake::keyPressEvent(QKeyEvent *event){
    QKeyEvent *key=(QKeyEvent*)event;
    switch (key->key()) {
    case Qt::Key_Up:nDirection=1;   //1代表上
        break;
    case Qt::Key_Down:nDirection=2;   //2代表下
        break;
    case Qt::Key_Left:nDirection=3;   //3代表左
        break;
    case Qt::Key_Right:nDirection=4;   //4代表右
        break;
    default:;
    }
}
QRect Snake::CreateRect(){//更新：丰富食物，让每次可以产生多个。
    int x,y;
    x=qrand()%75;//生成小于75的整数，为更新后变大的范围提供食物
    y=qrand()%75;

    QRect rect(20+x*10,20+y*10,10,10);//食物小方块位置
    x=qrand()%20;
    y=qrand()%20;
    QRect rect1(20+x*10,20+y*10,10,10);
    return rect;



    return rect1;
}
void Snake::IsEat(){
    if(SnakeHead==food){//如果蛇头和食物重合，说明已经撞到食物了
         SnakeHead=food;//吃到食物，食物就变为蛇头
         vSnakeRect.push_back(vSnakeRect.last());//将最后一个节点再次加到容器里，让蛇身变长
         food=CreateRect();//吃到食物后再生成一个食物
         nScore+=10;//得分
         if(speed>50){
             speed=speed-10;
             timer->stop();//停止当前计时器
             timer->start(speed);//设置新的计时器
         }
    }

}
void Snake::IsHit(){
    for(int i=1;i<vSnakeRect.size();i++){//遍历蛇身
        if(SnakeHead==vSnakeRect[i]){//蛇头和蛇身重合
            sDisplay="游戏结束";
            blsOver=true;
            update();
        }
    }
}
