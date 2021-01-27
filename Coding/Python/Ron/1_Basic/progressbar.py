import sys, time

'''
#方法一
#key是\r返回上一行並用新的內容覆蓋
利用標準輸出
sys.stdout.write(process_bar) #這兩句打印字符到終端
sys.stdout.flush()

import time
import sys
def progress_test():
  bar_length=20
  for percent in xrange(0, 100):
    hashes = '#' * int(percent/100.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
    sys.stdout.flush()
    time.sleep(1)
progress_test()
'''




class ShowProcess():
    """
    顯示處理進度的類
    調用該類相關函數即可實現處理進度的顯示
    """

    i = 0 # 當前的處理進度
    max_steps = 0 # 總共需要處理的次數
    max_arrow = 50 #進度條的長度
    infoDone = 'done'

    # 初始化函數，需要知道總共的處理次數
    def __init__(self, max_steps, infoDone = 'Done'):
        self.max_steps = max_steps
        self.i = 0
        self.infoDone = infoDone

    # 顯示函數，根據當前的處理進度i顯示進度
    # 效果為[>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else:
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #計算顯示多少個'>'
        num_line = self.max_arrow - num_arrow #計算顯示多少個'-'
        percent = self.i * 100.0 / self.max_steps #計算完成進度，格式為xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #帶輸出的字符串，'\r'表示不換行回到最左邊
        sys.stdout.write(process_bar) #這兩句打印字符到終端
        sys.stdout.flush()
        if self.i >= self.max_steps:
            self.close()

    def close(self):
        print('')
        print(self.infoDone)
        self.i = 0

if __name__=='__main__':
    max_steps = 100

    process_bar = ShowProcess(max_steps, 'OK')

    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.01)
