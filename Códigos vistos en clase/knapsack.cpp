#include <bits/stdc++.h>

using namespace std;

#define FIN ios::sync_with_stdio(0);cout.tie(0);cin.tie(0)

int main() {
	FIN;
	
	int n, w;
	cin >> n >> w;
	vector<int> p(n), v(n);
	for(int i = 0; i < n; i++) cin >> p[i];
	for(int i = 0; i < n; i++) cin >> v[i];
	
	vector <int> dp(w+1,-1); dp[0] = 0;
	for(int i = 0; i < n; i++) {
		vector<int> nextdp(w+1,-1);
		for(int peso = 0; peso <= w; peso++) {
			nextdp[peso] = dp[peso];
			if(peso - p[i] >= 0 and dp[peso-p[i]] != -1) {
				nextdp[peso] = max(nextdp[peso],dp[peso - p[i]] + v[i]);
			}
		}
		dp = nextdp;
	}
	cout << *max_element(dp.begin(),dp.end()) << "\n";
	
	
	return 0;
}
