import axios from 'axios';

class Api {
    baseAxios = axios.create({
        baseURL: 'http://jsonplaceholder.typicode.com/'
    });

    // Create another method for Master if changes are too extensive or if new api call is needed
    postTime (postObj) {
        return this.baseAxios.post(`/clockwerx/power`, {
            time: `${postObj.hours}:${postObj.minutes}:${postObj.seconds}`,
            fulltime: postObj.timerTime,
            id: postObj.id,
            status: postObj.status
        });
    }
};

export default new Api();