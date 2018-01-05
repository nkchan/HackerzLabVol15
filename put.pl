use strict;
use LWP::UserAgent;
use HTTP::Request::Common;


# URLを変更してください
my $url = 'https://9bqcyrr7bb.execute-api.ap-northeast-1.amazonaws.com/dev/Q14';
# POSTするデータを書き換えてください
my %postdata = ( 'id' => 'id', 'pass' => 'pass' );

# 一つなら
#my %postdata = ('id'=>'id')
#
my $request = POST( $url, \%postdata );

# 送信
my $ua = LWP::UserAgent -> new;
my $res = $ua -> request( $request ) -> as_string;
