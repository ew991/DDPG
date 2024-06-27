import h5py

# Đường dẫn tới tệp HDF5 của bạn
hdf5_path = 'saved_models\dqn\gneJ0.h5'
# hdf5_path = 'saved_models\dqn\gneJ6.h5'

with h5py.File(hdf5_path, 'r+') as f:
    # Kiểm tra và sửa đổi thuộc tính 'keras_version'
    if 'keras_version' in f.attrs:
        if isinstance(f.attrs['keras_version'], str):
            f.attrs['keras_version'] = f.attrs['keras_version'].encode('utf8')
    
    # Kiểm tra và sửa đổi thuộc tính 'backend'
    if 'backend' in f.attrs:
        if isinstance(f.attrs['backend'], str):
            f.attrs['backend'] = f.attrs['backend'].encode('utf8')
