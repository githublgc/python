#ifndef SNAKE_H
#define SNAKE_H

#include <QMainWindow>
#include<qpainter.h>
#include<QVector>
#include<qstring.h>
namespace Ui {
class Snake;
}

class Snake : public QMainWindow
{
    Q_OBJECT

public:
    explicit Snake(QWidget *parent = 0);
    ~Snake();
    void paintEvent(QPaintEvent *event);
    void InitSnake();//初始化蛇
    QRect CreateRect();
    void IsEat();
    void IsHit();

private slots:
    void Snake_update();//定义槽函数

private:
    Ui::Snake *ui;
    QVector<QRect> vSnakeRect;//蛇
    QRect SnakeHead;//蛇头
    void keyPressEvent(QKeyEvent *key);//定义键盘事件
    QTimer *timer;//定时器
    bool blsRun;//是否开始
    bool blsOver;//是否结束
    QString sDisplay;//开始结束提示
    int nDirection;//蛇移动的方向
    QRect food;//食物
    int nScore;//得分
    QString scoreLabel;//显示得分两个字
    int speed;//移动速度

};
#endif // SNAKE_H
