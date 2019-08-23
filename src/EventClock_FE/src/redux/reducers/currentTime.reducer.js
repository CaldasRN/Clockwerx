const defaultCurrentTime = {
    hours: '00',
    minutes: '00',
    seconds: '00',
    timerTime: 0,
};

const currentTime = (state = defaultCurrentTime, action) => {
    switch (action.type) {
        case 'CURRENT_TIME_HOURS':
            const newStateHrs = addTimeToState(state, 'hours', action.payload);
            console.log(newStateHrs);
            return newStateHrs;
        case 'CURRENT_TIME_MINUTES':
            const newStateMin = addTimeToState(state, 'minutes', action.payload);
            console.log(newStateMin);
            return newStateMin;
        case 'CURRENT_TIME_SECONDS':
            const newStateSec = addTimeToState(state, 'seconds', action.payload);
            console.log(newStateSec);
            return newStateSec;
        default:
            return state;
    }
}

function addTimeToState(currState, timeKey, timeValue) {
    const timeAsNumber = parseInt(timeValue);
    const timeDoubleDigit = makeTimeDoubleDigit(timeValue);
    const newTimeState = {
        ...currState,
    };
    newTimeState[timeKey] = timeDoubleDigit;
    newTimeState.timerTime = timeConverter(currState.timerTime, timeAsNumber, timeKey);
    return newTimeState;
}

function makeTimeDoubleDigit(timeStr) {
    let doubleDigit = '00';

    if (timeStr.length < 2 && timeStr.length !== 0) {
        doubleDigit = `0${timeStr}`;
    }

    return doubleDigit;
}

//TODO: Can remove baseTime from function
function timeConverter(baseTime, newTime, timeType) {
    let finalTime = 0;
    let conversion = 1;

    if (timeType === 'hours') {
        conversion = 1000 * 60 * 60;
    } else if (timeType === 'minutes') {
        conversion = 1000 * 60;
    } else if (timeType === 'seconds') {
        conversion = 1000;
    }
    finalTime = finalTime + (newTime * conversion);

    return finalTime;
}

export default currentTime;