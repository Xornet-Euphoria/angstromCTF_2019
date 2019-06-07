# Streams

## 手順
サイトにアクセスして開発者ツールを見るとstream.mp4というファイルが見つかるがこれを開こうとしても動画として再生できない。しかしResponce欄を覗いてみるとなぜかXML形式だった。  
ここで動画のストリーミングについて調べてみると.mpdというXML形式で書かれたプレイリストと.m4sという.mp4を断片化したファイルから成ることが判明。  
詳しく読んでみると初期化のためのinit-stream(0,1,2).m4sとchunk-stream(0,1,2)-0000(1,2,3...).m4sというファイルをストリーミングに使用していることがわかる。但し、(0,1,2)は0,1,2のいずれかで(1,2,3...)は1以上の整数。  
これらを全部ダウンロードするに当たってChromeの開発者ツールを用いていたところinit-stream2.m4sやchunk-stream2-00001.m4sといったstream2のファイルが再生されていない(ブラウザが読んでいない)ことがわかる。  
これらは再生されないもののダウンロードは可能だったのであるだけ落としてくる。
ここでストリーミングについて調べてみるとストリーミングで使われるm4sファイルはmp4を分割しただけであることが判明。  
initを先頭に後は数字順に繋げて拡張子をmp4に変更したところ再生でき、動画ではなく音声を得ることができた。
これをmp3に変換し波形を見るとおそらくモールス信号だと思ったので符号に直して文字列と対応させるとフラグが出てくる(途中のハイフンをアンダースコアに、通常の括弧を波括弧に変換した)。  
なおバイナリファイルの結合にはbin_combine.py(同一ディレクトリ内に添付)を使用した。

## Flag
actf{f145h_15_d34d_10n9_11v3_mp39_d45h}

## 参考文献
- フロントエンドエンジニアのための動画ストリーミング技術基礎  
(https://ygoto3.com/posts/streaming-technology-basics-for-frontend-engineers/ )
- Combine MPEG-DASH segments (ex, init.mp4 + segments.m4s) back to a full source.mp4? - Stack Overflow  
(https://stackoverflow.com/questions/23485759/combine-mpeg-dash-segments-ex-init-mp4-segments-m4s-back-to-a-full-source-m )
