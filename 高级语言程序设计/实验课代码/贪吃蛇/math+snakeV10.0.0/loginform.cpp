#include "loginform.h"
#include <QMessageBox>
#include<QPixmap>
#include<qpainter.h>
void LoginForm::paintEvent(QPaintEvent *event){
QPainter painter(this);
painter.drawPixmap(15,15,300,300,QPixmap(":/myImage/image/nku.png"));}//给登陆界面加上背景校徽
LoginForm::LoginForm(QDialog *parent) ://注意，这里设置用户名为 南小开 密码 1919
    QDialog(parent)
{
    //设置窗体标题
    this->setWindowTitle(tr("娱乐天地"));

    //
    userNameLbl = new QLabel(this);   //new一个标签对象
    userNameLbl->move(50,80);
    userNameLbl->setText("用户:");  //设置标签文本

    //用户名输入
    userNameLEd = new QLineEdit(this);
    userNameLEd->move(120,80);
    userNameLEd->setPlaceholderText(tr("cin your user name"));//占位符

    //
    pwdLbl = new QLabel(this);
    pwdLbl->move(50,130);
    pwdLbl->setText("密码:");

    //密码输入
    pwdLEd = new QLineEdit(this);
    pwdLEd->move(120,130);
    pwdLEd->setPlaceholderText("cin your text");
    pwdLEd->setEchoMode(QLineEdit::PasswordEchoOnEdit);//改进：输入的密码输入时可见，否则小黑点。PasswordEchoOnEdit

    //登录按钮
    loginBtn = new QPushButton(this);
    loginBtn->move(40,200);
    loginBtn->setText("进入游戏");//趣味性元素融入大作业中，算是个小彩蛋吧，嘿嘿！

    //退出按钮
    exitBtn = new QPushButton(this);
    exitBtn->move(190,200);
    exitBtn->setText("回去学习");

    //增设：提示hint按键
    hintBtn = new QPushButton(this);
    hintBtn->move(120,270);
    hintBtn->setText("hint");


    // 执行 LoginForm::login 槽函数(自定义)；
    connect(loginBtn,&QPushButton::clicked,this,&LoginForm::login);
    connect(exitBtn,&QPushButton::clicked,this,&LoginForm::close);
    connect(hintBtn,&QPushButton::clicked,this,&LoginForm::hint);// 新增设提示密码功能


}

void LoginForm::hint()//实现弹出2.在CPP里加声明
{QMessageBox::warning(this, tr("提示"),tr("TIPS:建校时间"),QMessageBox::Yes);}


void LoginForm::login()
{
    //获得userNameLEd输入框的文本：userNameLEd->text()；
    //trimmed()去掉前后空格

    if(userNameLEd->text().trimmed() == tr("南小开") && pwdLEd->text() == tr("1919"))
    {
       accept();//关闭窗体，并设置返回值为Accepted
    }
    else
    {                              //标题              内容                OK按钮,界面内容的优化
        QMessageBox::warning(this, tr("错误"),tr("TIPS:允公允能"),QMessageBox::Yes);//加入南开校训文化

    // 清空输入框内容
       userNameLEd->clear();
       pwdLEd->clear();

       //光标定位
       userNameLEd->setFocus();
    }
}
