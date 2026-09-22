class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        SegTree tree(nums, k);

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int idx = q[0], val = q[1], start = q[2], x = q[3];
            tree.update(idx, val);
            ans.push_back(tree.query(start, n - 1).cnt[x]);
        }
        return ans;
    }

private:
    struct Info {
        int prod = 1;
        int cnt[5] = {0, 0, 0, 0, 0}; // k <= 5, so a fixed-size array is fine
    };

    struct SegTree {
        int n, k;
        vector<Info> tr;

        SegTree(vector<int>& nums, int k_) : k(k_) {
            n = nums.size();
            tr.assign(4 * n, Info());
            build(1, 0, n - 1, nums);
        }

        Info combine(const Info& L, const Info& R) {
            Info res;
            res.prod = (int)((long long)L.prod * R.prod % k);
            for (int r = 0; r < k; ++r) res.cnt[r] = L.cnt[r];
            for (int r = 0; r < k; ++r) {
                if (R.cnt[r]) {
                    int bucket = (int)((long long)L.prod * r % k);
                    res.cnt[bucket] += R.cnt[r];
                }
            }
            return res;
        }

        void build(int node, int lo, int hi, vector<int>& nums) {
            if (lo == hi) {
                int v = nums[lo] % k;
                tr[node].prod = v;
                tr[node].cnt[v] = 1;
                return;
            }
            int mid = (lo + hi) / 2;
            build(2 * node, lo, mid, nums);
            build(2 * node + 1, mid + 1, hi, nums);
            tr[node] = combine(tr[2 * node], tr[2 * node + 1]);
        }

        void update(int pos, int value, int node, int lo, int hi) {
            if (lo == hi) {
                int v = value % k;
                tr[node].prod = v;
                for (int r = 0; r < k; ++r) tr[node].cnt[r] = 0;
                tr[node].cnt[v] = 1;
                return;
            }
            int mid = (lo + hi) / 2;
            if (pos <= mid) update(pos, value, 2 * node, lo, mid);
            else update(pos, value, 2 * node + 1, mid + 1, hi);
            tr[node] = combine(tr[2 * node], tr[2 * node + 1]);
        }
        void update(int pos, int value) { update(pos, value, 1, 0, n - 1); }

        Info query(int l, int r, int node, int lo, int hi) {
            if (l <= lo && hi <= r) return tr[node];
            int mid = (lo + hi) / 2;
            if (r <= mid) return query(l, r, 2 * node, lo, mid);
            if (l > mid) return query(l, r, 2 * node + 1, mid + 1, hi);
            return combine(query(l, r, 2 * node, lo, mid),
                           query(l, r, 2 * node + 1, mid + 1, hi));
        }
        Info query(int l, int r) { return query(l, r, 1, 0, n - 1); }
    };
};