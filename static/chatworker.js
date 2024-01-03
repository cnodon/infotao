self.onmessage = async function (e) {
    const url = e.data;

    console.log('Worker received URL:', url);

};