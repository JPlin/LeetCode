class MyCalendar {

    private TreeMap<Integer, Integer> startMap;
    public MyCalendar() {
        startMap = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        Integer nextStart = startMap.ceilingKey(start);
        if (nextStart != null && nextStart < end) {
            return false;
        }
        Integer prevStart = startMap.lowerKey(start);
        if(prevStart != null && startMap.get(prevStart) > start) {
            return false;
        }
        startMap.put(start, end);
        return true;
    }
