# 量子コンピュータ
# qubitと言う0かも知れないし1かも知れないと言う厄介なビットを用いる
# 回路を組み合わせて計算して問題を解決するらしい
# 
# 1qubitのゲート
# Xゲート 要はNOTゲート、0を1に、1を0にする
# H(アダマール)ゲート 0と1が重なった状態になる
# 位相ゲート 位相差を変化させるゲート、ググったけどよくわからない
# 
# 2qubitのゲート
# C-NOTゲート 片方のビットが1ならばもう片方を反転させるゲート
#            こいつのおかげで重ね合わせが可能になって、並列して結果を出していける





from blueqat import Circuit

# Circuit 回路を用意
# m 観測、結果を確定
# [:] 全てのビットにゲートを適用
# run(shots=xxx) 計算をxxx回行う

#1qubit shotsは計算する回数
# Xゲート 反転させる
print(Circuit().x[0].m[:].run(shots=100)) 
# Hゲート 半々の状態　重ね合わせ
print(Circuit().h[0].m[:].run(shots=100)) 


#2qubit
# C-NOTゲート 制御ビットが0なので00となる
print(Circuit().cx[0,1].m[:].run(shots=100))

# C-NOTゲート 制御ビットを反転させて0なので00となる
print(Circuit().x[0].cx[0,1].m[:].run(shots=1)) 

#ビット数指定 最後のビットは使われず
print(Circuit(3).x[0].cx[0,1].m[:].run(shots=1))

# Zゲート、負の数にする（結果では±の判別がつかないのでベクトルで出すこと）
print(Circuit().h[0].z[0].m[:].run(shots=100))
print(Circuit().h[0].z[0].run())

# 重ね合わせ ビットの全ての状態 00 01 10 11 が計算される
print(Circuit().h[0,1].m[:].run(shots=100))

# 量子もつれ 0番目が0なら1番目も0、1番目が1なら0番目も1の時を表す
print(Circuit().h[0].cx[0,1].m[:].run(shots=100))