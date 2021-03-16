#include <bits/stdc++.h>
using namespace std;

typedef long long           ll;
typedef long double         ld;
typedef unsigned long       ul;
typedef unsigned long long  ull;
typedef vector<ll>          vll;
typedef vector<int>         vi;
typedef pair<int,int>       pii;
typedef pair<ll,ll>         pll;
typedef pair<ld,ld>         pld;
typedef vector< pii >       vii;

#define fastIO              ios::sync_with_stdio(false);    cin.tie(nullptr);   cout.tie(nullptr)
#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize("unroll-loops")
#pragma G++ optimize("Ofast,no-stack-protector")
#pragma G++ target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma G++ optimize("unroll-loops")

#define MX                  INT_MAX
#define MN                  INT_MIN
#define MAX                 200005
#define MOD                 1000000007
#define eps                 1e-9
#define INF                 0x3f3f3f3f3f3f3f3f /// 4,557,430,888,798,830,399
#define inf                 0x3f3f3f3f /// 1,061,109,567
#define PI                  acos(-1.0)  /// 3.1415926535897932

#define pb                  push_back
#define ppb                 pop_back
#define mp                  make_pair
#define ff                  first
#define ss                  second
#define sf                  scanf
#define pf                  printf
#define pn                  pf("\n")
#define sfi(x)              sf("%d", &x)
#define sfii(x, y)          sf("%d %d", &x, &y)
#define sfiii(x, y, z)      sf("%d %d %d", &x, &y, &z)
#define sfl(x)              sf("%lld", &x)
#define sfll(x, y)          sf("%lld %lld", &x, &y)
#define sflll(x, y, z)      sf("%lld %lld %lld", &x, &y, &z)
#define pfi(x)              pf("%d\n", x)
#define pfii(x, y)          pf("%d %d\n", x, y)
#define pfiii(x, y, z)      pf("%d %d %d\n", x, y, z)
#define pfl(x)              pf("%lld\n", x)
#define pfll(x, y)          pf("%lld %lld\n", x, y)
#define pflll(x, y, z)      pf("%lld %lld %lld\n", x, y, z)
#define gl(a)               getline(cin,a)
#define pfs(a)              pf("%s\n", a)
#define pfc(a)              pf("%c", a)
#define yes                 pf("YES\n")
#define no                  pf("NO\n")
#define sqr(x)              ((x)*(x))
#define loop(i, y)          for(int i=0; i<int(y); i++)
#define FOR(i, x, y)        for(int i=int(x); i<=int(y); i++)
#define ROF(i, x, y)        for(int i=int(x); i>=int(y); i--)
#define all(c)              c.begin(), c.end()
#define sz(c)               int(c.size())
#define clr(x, y)           memset(x, y, sizeof(x))
#define vin(v, y)           int w; for(int i=0;i<y;i++){ sf1(w); v.pb(w);}
#define vout(v)             int g=v.size(); for(int i=0;i<g;i++){ pf("%d", v[i]); if(i<g-1) pf(" "); else pf("\n");}
#define voutr(v)            int g=v.size(); for(int i=g-1;i>=0;i--){ pf("%d", v[i]); if(i>0) pf(" "); else pf("\n");}
#define test(tt)            for(int cas=1;cas<=tt;cas++)
#define max3(a,b,c)         max(max(a,b),c)
#define max4(a,b,c,d)       max(max3(a,b,c),d)
#define min3(a,b,c)         min(min(a,b),c)
#define min4(a,b,c,d)       min(min3(a,b,c),d)
#define even(n)             if(n%2==0)
#define odd(n)              if(n%2==1)

template <class T> inline T bigMod(T p,T e,T M){ T ret = 1; for(; e > 0; e >>= 1){ if(e & 1) ret = (ret * p) % M; p = (p * p) % M; } return (T) ret;}
template <class T> inline T modInverse(T a,T M){return bigMod(a,M-2,M);}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/gcd(a,b))*b;}
template <class T> inline bool isprime(T n){if(n<2)return false;for(ll i=2;i*i<=n;i++){if(n%i==0)return false;}return true;}
#define input               freopen("input.txt","r",stdin);
#define output              freopen("output.txt","w",stdout);
/* //////////////////////////START\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ */
int main()
{
    #ifdef VAMP
        clock_t tStart = clock();
        //input;
        //output
    #endif
	int t;
	sfi(t);
	while(t--){
		ll a, b;
		sfll(a,b);
		if(gcd(a, b)==1){
			cout << "Nao" <<endl;
		}
		else cout << "Sim" <<endl;
	}
	#ifdef VAMP
        printf("\nRuntime:: %.10fs\n", (double)(clock()-tStart)/CLOCKS_PER_SEC);
    #endif
    return 0;
}
