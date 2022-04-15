#ifndef LOGINFORM_H
#define LOGINFORM_H
#include<qpainter.h>


#include <QDialog>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>


class LoginForm : public QDialog
{
    Q_OBJECT //使用信号与槽需要的宏
public:
    explicit LoginForm(QDialog *parent = 0);
    void paintEvent(QPaintEvent *event);
signals:

public slots:
    void login();//点击登录按钮是执行的槽函数
    void  hint();//实现弹窗3，在.h里声明。
private:
    QLabel *userNameLbl;         //"用户名"标签
    QLabel *pwdLbl;              //"密码"标签
    QLineEdit *userNameLEd;      //用户名编辑行
    QLineEdit *pwdLEd;           //密码编辑行
    QPushButton *loginBtn;       //登录按钮
    QPushButton *exitBtn;        //退出按钮
    QPushButton *hintBtn;       //提示按钮

};

#endif // LOGINFORM_H
