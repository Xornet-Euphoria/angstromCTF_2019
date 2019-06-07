# Printer Pager

## 手順
パケットを解析するとプリンターにページ数や使用用紙等のプリンタジョブを制御する情報を送るPJLが書かれた部分と印刷対象のデータが書かれた部分がある。  
このデータが書かれた部分はPDFそのものであったりPostScriptといったような描画用の言語だったりする。  
今回のパケットを見るとPJL部分から使われているプリンターがLaserJet P1505nだとわかる。  
データ部分のマジックナンバーは`2C 58 51 58`であり、文字列にすると`,XQX`。  
XQXで検索をかけてみると今回使われているプリンターへ送る描画用の言語が.xqxという形式であることがわかる。
PostScript -> xqxファイルの変換をするプログラムfoo2xqxとxqx -> PostScriptの変換をするプログラム、xqxdecodeまでGithubに用意されているので手順に従ってインストールする。  
パケット解析に戻り、xqxファイル部分だと思われる箇所を全てエクスポート(Wiresharkを使用した)して順番に結合する。  
これをxqxdecodeに渡し`./xqxdecode -d output input`のようにして実行するとoutput.pbmが読める形で降ってくるのでそれを開くとフラグが載っている。  
なお、バイナリ結合にはStreamsで用いたbin_combine.pyを使用した。

## Flag
actf{daniel_zhu_approves}

## 参考文献
- PJL - Wikipedia  
(https://ja.wikipedia.org/wiki/PJL)
- koenkooi/foo2zjs - GitHub  
(https://github.com/koenkooi/foo2zjs)
