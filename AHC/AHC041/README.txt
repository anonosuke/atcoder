<div class="part">
<section>
<h3>ストーリー</h3><p>AtCoderオフィスでは、一足遅いクリスマスパーティーの準備が進められている。高橋社長は、クリスマスツリーに使う根付き木を切りに行くことにした。</p>
<p>根付き木の各頂点は <strong>美しさ</strong> を持ち、高いところに美しい頂点が存在するとパーティー会場の <strong>見栄え</strong> が良くなる。ただし、根付き木が高すぎるとAtCoderオフィスの天井にぶつかってしまうため、パーティー会場に持ち込むことのできる根付き木の高さには制限がかけられている。</p>
<p>与えられたグラフから根付き木をいくつか切り出して、できるだけパーティー会場の <strong>見栄え</strong> を良くして欲しい。</p>
</section>
</div>

<div class="part">
<section>
<h3>問題文</h3><p><var>N</var> 頂点 <var>M</var> 辺の連結な無向平面グラフ <var>G</var> が与えられる。頂点には <var>0</var> から <var>N-1</var> の番号が、辺には <var>0</var> から <var>M-1</var> の番号がそれぞれ付けられている。頂点 <var>v</var> の座標は <var>(x_v, y_v)</var> であり、 辺 <var>i</var> は頂点 <var>u_i</var> と <var>v_i</var> を結んでいる。各頂点には正の整数をとる <strong>美しさ</strong> が定められており、頂点 <var>v</var> の <strong>美しさ</strong> は <var>A_v</var> である。</p>
<p>根付き木 <var>T</var> の <strong>見栄え</strong> を以下のように定義する。
<var>T</var> における頂点 <var>v</var> の <strong>高さ</strong> <var>h_v</var> を、根から <var>v</var> へのパスに含まれる辺の本数とする。
このとき、根付き木 <var>T</var> の <strong>見栄え</strong> <var>a(T)</var> は <var>a(T):=\sum_{v\in T} (h_v + 1) A_v</var> と定義される。</p>
<p>与えられたグラフ <var>G</var> から以下の条件を満たすような根付き木の集合を構築し、<strong>見栄え</strong> の総和をできるだけ大きくせよ。</p>
<ul>
<li>各根付き木 <var>T</var> に含まれる辺は全て <var>G</var> に含まれる。</li>
<li><var>G</var> の各頂点はちょうど <var>1</var> つの根付き木に属する。</li>
<li>各根付き木における頂点の高さは全て <var>H</var> 以下である。</li>
</ul>
</section>
</div>

<div class="part">
<section>
<h3>得点</h3><p>出力した根付き木の集合を <var>F</var> としたとき、<var>1+\sum_{T\in F}a(T)</var> の得点が得られる。</p>
<p>合計で 150 個のテストケースがあり、各テストケースの得点の合計が提出の得点となる。
一つ以上のテストケースで不正な出力や制限時間超過をした場合、提出全体の判定が<span class='label label-warning' data-toggle='tooltip' data-placement='top' title="不正解">WA</span>や<span class='label label-warning' data-toggle='tooltip' data-placement='top' title="実行時間制限超過">TLE</span>となる。
コンテスト時間中に得た最高得点で最終順位が決定され、コンテスト終了後のシステムテストは行われない。 同じ得点を複数の参加者が得た場合、提出時刻に関わらず同じ順位となる。</p>
</section>
</div>

<hr />
<div class="io-style">
<div class="part">
<section>
<h3>入力</h3><p>入力は以下の形式で標準入力から与えられる。</p>
<pre><var>N</var> <var>M</var> <var>H</var>
<var>A_0</var> <var>\cdots</var> <var>A_{N-1}</var>
<var>u_0</var> <var>v_0</var>
<var>\vdots</var>
<var>u_{M-1}</var> <var>v_{M-1}</var>
<var>x_0</var> <var>y_0</var>
<var>\vdots</var>
<var>x_{N-1}</var> <var>y_{N-1}</var>
</pre>
<p>入力は以下の制約を満たす。</p>
<ul>
<li><var>N=1000</var></li>
<li><var>1000\le M \le 3000</var></li>
<li><var>H=10</var></li>
<li><var>1\le A_v\le 100</var></li>
<li><var>0\le u_i \lt v_i\le N-1</var></li>
<li><var>0\le x_v, y_v\le 1000</var></li>
<li><var>(x_v, y_v)</var> は全て異なる。</li>
<li>入力は全て整数。</li>
<li>与えられるグラフは連結な平面グラフであり、頂点 <var>v</var> を座標 <var>(x_v, y_v)</var> に配置し、各辺を両端点を結ぶ線分として描画した時、どの二辺も端点以外に共通点を持たないことが保証されている。</li>
</ul>
</section>
</div>

<div class="part">
<section>
<h3>出力</h3><p>構築した根付き木の集合における頂点 <var>v</var> の親の頂点番号を <var>p_v</var>（<var>v</var> が根の場合は <var>p_v=-1</var>）として、以下の形式で標準出力に出力せよ。</p>
<pre><var>p_0</var> <var>p_1</var> <var>\cdots</var> <var>p_{N-1}</var>
</pre>
<p><a href="https://img.atcoder.jp/ahc041/m0Bwp9WL.html?lang=ja&seed=0&output=sample">例を見る</a></p>
<p>解は複数回出力しても良い。 複数出力された場合、一番最後に出力された解のみが採点に用いられる。 Web版のビジュアライザを用いると、複数の解の比較が可能である。</p>
</section>
</div>
