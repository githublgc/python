#ifndef MAINFORM_H
#define MAINFORM_H
#include <QDialog>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMainWindow>//对欢迎界面进行改进，增加按钮来实现界面跳转。
#include <QLabel>
#include<qpainter.h>
#include<secondwidget.h>

class MainForm : public QDialog
{
    Q_OBJECT //使用信号与槽需要的宏
public:
    explicit MainForm(QWidget *parent = 0);

signals:

public slots:
    void login1();//点击登录按钮是执行的槽函数
    void login2();//点击登录按钮是执行的槽函数

private:
    QLabel *tipLbl;  //"欢迎登录"标签
    QPushButton *login2Btn;         //计算器按钮
    QLabel *userNameLbl;
    QLabel *pwdLbl;
    QLineEdit *userNameLEd;
    QLineEdit *pwdLEd;           //密码编辑行
    QPushButton *login1Btn;       //贪吃蛇按钮
    QPushButton *exitBtn;        //退出按钮
    QPushButton *hintBtn;       //提示按钮
    QPushButton*  btn1;

};

#endif // MAINFORM_H
