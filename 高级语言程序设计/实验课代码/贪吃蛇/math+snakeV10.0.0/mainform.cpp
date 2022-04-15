#include "mainform.h"
#include <QMessageBox>//增加下一步选择游戏模式和进行游戏的功能，本篇修改了几乎所有的内容
#include"loginform.h"

#pragma comment  (lib, "User32.lib")
#include "mainform.h"
/*LoginForm::LoginForm(QDialog *parent) ://改进：注意，   不再使用
    QDialog(parent)
{

    // 执行 LoginForm::login 槽函数(自定义)；
    connect(loginBtn,&QPushButton::clicked,this,&LoginForm::login);
    connect(exitBtn,&QPushButton::clicked,this,&LoginForm::close);



}  */


/*void LoginForm::login()
{
    //获得userNameLEd输入框的文本：userNameLEd->text()；
    //trimmed()去掉前后空格

    if(userNameLEd->text().trimmed() == tr("nku") && pwdLEd->text() == tr("1919"))
    {
       accept();//关闭窗体，并设置返回值为Accepted
    }
    else
    {                              //标题              内容                OK按钮,界面内容的优化
        QMessageBox::warning(this, tr("warning"),tr("wrong"),QMessageBox::Yes);

    // 清空输入框内容
       userNameLEd->clear();
       pwdLEd->clear();

       //光标定位
       userNameLEd->setFocus();
    }
} */

/*Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    layout1=new QHBoxLayout;
    layout2=new QHBoxLayout;

    layout4=new QGridLayout(this);

    btn1=new QPushButton;
    edit1=new QLineEdit;
    edit2=new QLineEdit;
    edit3=new QLineEdit;
     label1=new QLabel;


 layout4->addWidget(btn1,0,0);
 layout4->addWidget(edit1,0,1);
 layout4->addWidget(edit2,0,2);
 layout4->addWidget(edit3,0,3);

  layout4->addWidget(label1,1,2);
   btn1->setText("计算");

connect(btn1,SIGNAL(clicked()),this,SLOT(on_clicked()));
}

Widget::~Widget()
{

}
void Widget::on_clicked()
{
       int a = edit1->text().toInt();//第一个空输入
        int b = edit3->text().toInt();//后一个操作数在第三个上面的输入
        if (edit2->text() == "+")//通过分析第二个空输入的字符来判断进行什么功能
            label1->setText(QString::number(a + b));
        if (edit2->text() == "-")
            label1->setText(QString::number(a - b));
        if (edit2->text() == "*")
            label1->setText(QString::number(a * b));
        if (edit2->text() == "/")
        {
            if (b != 0)
                label1->setText(QString::number(a / b));
        }
        if (edit2->text() == "%")//     增加新功能
        {
            if (b != 0)
                label1->setText(QString::number(a % b));
        }
}*/




MainForm::MainForm(QWidget *parent) ://注意，在第二个界面需要最大化看所有功能
    QDialog(parent)
{

    tipLbl = new QLabel(this);
    tipLbl->setText(tr("游戏模式"));
    //设置窗体标题
    this->setWindowTitle(tr("选择游戏"));

    //
    userNameLbl = new QLabel(this);   //new一个标签对象
    userNameLbl->move(50,80);
    userNameLbl->setText("南小开");  //设置标签文本

    //操作数1输入
    userNameLEd = new QLineEdit(this);
    userNameLEd->move(120,80);
    userNameLEd->setPlaceholderText(tr("日新月异"));//

    //
    pwdLbl = new QLabel(this);
    pwdLbl->move(50,130);
    pwdLbl->setText("西南联大");

    //操作数2输入
    pwdLEd = new QLineEdit(this);
    pwdLEd->move(120,130);
    pwdLEd->setPlaceholderText("刚毅坚卓");
    pwdLEd->setEchoMode(QLineEdit::Normal);//改进：保持一直可见

    //结果是奇数的按钮
    login1Btn = new QPushButton(this);
    login1Btn->move(40,300);
    login1Btn->setText("snake");

    //结果是偶数的按钮
    login2Btn = new QPushButton(this);
    login2Btn->move(190,300);
    login2Btn->setText("math");

    //退出按键
    exitBtn = new QPushButton(this);
    exitBtn->move(120,370);
    exitBtn->setText("我爱学习!");

    //接下来实现向游戏界面跳转的问题。
    connect(exitBtn,&QPushButton::clicked,this,&LoginForm::close);


    connect(login1Btn,&QPushButton::clicked,this,&MainForm::login1);
    connect(login2Btn,&QPushButton::clicked,this,&MainForm::login2);

}
void MainForm::login2()//实现弹出2.在CPP里加声明!!!特别注意，需要在函数体里声明下面的函数才能取消报错！！

{accept();}//就是关闭了当前窗口，向下一个进行。

void MainForm::login1()//实现弹出2.在CPP里加声明!!!特别注意，需要在函数体里声明下面的函数才能取消报错！！

{accept();}
